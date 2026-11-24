import json
from pathlib import Path
from datetime import datetime
LIMITES={"P1":4,"P2":8,"P3":24,"P4":48}
def avaliar(chamado, agora=None):
    inicio=datetime.fromisoformat(chamado["aberto"])
    fim=datetime.fromisoformat(chamado["resolvido"]) if chamado.get("resolvido") else agora
    if fim is None or inicio.tzinfo is None or fim.tzinfo is None or fim<inicio:
        raise ValueError("Datas invalidas")
    horas=(fim-inicio).total_seconds()/3600
    return {"id":chamado["id"],"horas":horas,"sla":"VENCIDO" if horas>LIMITES[chamado["prioridade"]] else "NO_PRAZO"}
if __name__=="__main__":
    print(json.dumps([avaliar(c) for c in json.loads(Path("chamados.json").read_text())],indent=2))
