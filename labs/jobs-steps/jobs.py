import json
from dataclasses import dataclass

@dataclass
class Step:
    nome: str
    executar: object
    deps: tuple = ()
    tentativas: int = 2

def rodar(steps):
    mapa = {s.nome: s for s in steps}
    if len(mapa) != len(steps):
        raise ValueError("Step duplicado")
    ordem, visitando, vistos = [], set(), set()
    def visitar(nome):
        if nome in visitando:
            raise ValueError("Ciclo nas dependencias")
        if nome in vistos:
            return
        if nome not in mapa:
            raise ValueError("Dependencia desconhecida")
        s = mapa[nome]
        if type(s.tentativas) is not int or s.tentativas < 1:
            raise ValueError("Tentativas invalidas")
        visitando.add(nome)
        for dep in s.deps:
            visitar(dep)
        visitando.remove(nome)
        vistos.add(nome)
        ordem.append(nome)
    for nome in mapa:
        visitar(nome)
    resultado = {}
    for nome in ordem:
        s = mapa[nome]
        if any(resultado[d]["estado"] != "OK" for d in s.deps):
            resultado[nome] = {"estado": "BLOQUEADO", "tentativas": 0}
            continue
        for n in range(1, s.tentativas + 1):
            try:
                s.executar()
                resultado[nome] = {"estado": "OK", "tentativas": n}
                break
            except Exception as e:
                resultado[nome] = {"estado": "FALHA", "tentativas": n, "erro": type(e).__name__}
    return resultado

if __name__ == "__main__":
    contador = [0]
    def transitoria():
        contador[0] += 1
        if contador[0] == 1:
            raise RuntimeError("Falha ficticia")
    print(json.dumps(rodar([Step("extrair", lambda: None), Step("validar", transitoria, ("extrair",)), Step("consolidar", lambda: None, ("validar",))]), indent=2))
