import json
import time
import urllib.parse
import urllib.request
import uuid

loki="http://127.0.0.1:13100"
otlp="http://127.0.0.1:14318/v1/logs"
for _ in range(90):
    try:
        with urllib.request.urlopen(loki+"/ready",timeout=2) as r:
            if r.status==200:
                break
    except OSError:
        pass
    time.sleep(1)
else:
    raise RuntimeError("Loki indisponivel")
evento="INC-DEMO-"+uuid.uuid4().hex
agora=time.time_ns()
payload={"resourceLogs":[{"resource":{"attributes":[{"key":"service.name","value":{"stringValue":"portal-demo"}}]},"scopeLogs":[{"scope":{"name":"profox-lab"},"logRecords":[{"timeUnixNano":str(agora),"severityNumber":9,"severityText":"INFO","body":{"stringValue":evento}}]}]}]}
req=urllib.request.Request(otlp,data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
for _ in range(30):
    try:
        with urllib.request.urlopen(req,timeout=3) as r:
            resp=json.load(r)
            assert not resp.get("partialSuccess",{}).get("rejectedLogRecords",0)
        break
    except OSError:
        time.sleep(1)
else:
    raise RuntimeError("Collector indisponivel")
for _ in range(60):
    q=urllib.parse.urlencode({"query":'{service_name="portal-demo"} |= "'+evento+'"',"start":str(agora-60_000_000_000),"end":str(time.time_ns()),"limit":10})
    with urllib.request.urlopen(loki+"/loki/api/v1/query_range?"+q,timeout=5) as r:
        result=json.load(r)
    if any(evento in linha for s in result["data"]["result"] for _,linha in s["values"]):
        print("Log OTLP localizado no Loki")
        break
    time.sleep(1)
else:
    raise AssertionError("Log nao encontrado")
