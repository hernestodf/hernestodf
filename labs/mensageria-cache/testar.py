import base64
import json
import subprocess
import time
import urllib.request

base = "http://127.0.0.1:15682/api/"
def api(path, method="GET", data=None):
    req = urllib.request.Request(base + path, method=method,
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": "Basic " + base64.b64encode(b"demo:somente-lab").decode(), "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=3) as r:
        body = r.read()
        return json.loads(body) if body else None

def redis(*args):
    return subprocess.check_output(["docker","compose","exec","-T","redis","redis-cli","--raw",*args], text=True).strip()

for _ in range(60):
    try:
        api("overview")
        break
    except (OSError, ValueError):
        time.sleep(1)
else:
    raise RuntimeError("RabbitMQ indisponivel")
api("queues/%2F/chamados-demo", "PUT", {"durable":False,"auto_delete":False,"arguments":{}})
assert api("exchanges/%2F/amq.default/publish","POST",{"properties":{},"routing_key":"chamados-demo","payload":"INC-DEMO-001","payload_encoding":"string"})["routed"]
msg = api("queues/%2F/chamados-demo/get","POST",{"count":1,"ackmode":"ack_requeue_false","encoding":"auto","truncate":1000})
assert msg[0]["payload"] == "INC-DEMO-001"
assert api("queues/%2F/chamados-demo/get","POST",{"count":1,"ackmode":"ack_requeue_false","encoding":"auto","truncate":1000}) == []
assert redis("SET","demo:status","OK","EX","3") == "OK"
assert redis("GET","demo:status") == "OK"
time.sleep(4)
assert redis("EXISTS","demo:status") == "0"
print("Fila e expiracao de cache validadas")
