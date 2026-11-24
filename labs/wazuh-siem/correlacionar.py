import json
from collections import defaultdict, deque
from pathlib import Path

def correlacionar(eventos, limite=5, janela=60):
    if limite < 1 or janela < 1:
        raise ValueError("Limites invalidos")
    filas = defaultdict(deque)
    alertas = []
    for e in sorted(eventos,key=lambda e:e["segundo"]):
        if e["evento"] != "ssh_failure":
            continue
        q = filas[e["ip"]]
        while q and e["segundo"]-q[0] > janela:
            q.popleft()
        q.append(e["segundo"])
        if len(q) == limite:
            alertas.append({"ip":e["ip"],"segundo":e["segundo"],"tipo":"SSH_REPETIDO"})
    return alertas
if __name__ == "__main__":
    print(json.dumps(correlacionar(json.loads(Path("eventos.json").read_text())),indent=2))
