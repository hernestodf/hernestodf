import json
import time
import urllib.parse
import urllib.request
import urllib.error
base = "http://127.0.0.1:18082/realms/profox-demo"
for _ in range(90):
    try:
        with urllib.request.urlopen(base+"/.well-known/openid-configuration",timeout=3) as r:
            cfg=json.load(r)
        break
    except OSError:
        time.sleep(2)
else:
    raise RuntimeError("Keycloak indisponivel")
assert cfg["issuer"] == base
def token(secret):
    body=urllib.parse.urlencode({"grant_type":"client_credentials","client_id":"servico-demo","client_secret":secret}).encode()
    with urllib.request.urlopen(cfg["token_endpoint"],data=body,timeout=5) as r:
        return json.load(r)
assert token("somente-lab")["access_token"]
try:
    token("incorreto")
except urllib.error.HTTPError as e:
    assert e.code in (400,401)
else:
    raise AssertionError("Segredo invalido aceito")
print("Discovery, token e rejeicao de credencial validados")
