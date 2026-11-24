import json
from pathlib import Path

def auditar(dados):
    alertas = []
    for u in dados["usuarios"]:
        if u["mfa"] is not True:
            alertas.append({"alvo": u["login"], "risco": "MFA_AUSENTE"})
        if u["admin"] is True:
            alertas.append({"alvo": u["login"], "risco": "REVISAR_PRIVILEGIO"})
    for r in dados["recursos"]:
        if r["armazenamento_publico"] is True:
            alertas.append({"alvo": r["nome"], "risco": "ARMAZENAMENTO_PUBLICO"})
        if r["administracao_aberta"] is True:
            alertas.append({"alvo": r["nome"], "risco": "ADMINISTRACAO_ABERTA"})
    return alertas

if __name__ == "__main__":
    dados = json.loads(Path(__file__).with_name("inventario.json").read_text(encoding="utf-8"))
    print(json.dumps(auditar(dados), indent=2, ensure_ascii=False))
