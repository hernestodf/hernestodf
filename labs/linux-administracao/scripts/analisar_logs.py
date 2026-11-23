#!/usr/bin/env python3
"""Analisa logs fictícios, sem rede, dependências externas ou alteração de arquivos."""
import argparse
import collections
import json
import re
from pathlib import Path

PADRAO = re.compile(r"^(?P<data>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) (?P<nivel>INFO|WARNING|ERROR|CRITICAL) (?P<mensagem>.+)$")
NIVEIS = ("INFO", "WARNING", "ERROR", "CRITICAL")


def analisar(caminho: Path) -> dict:
    contagem = collections.Counter()
    eventos_criticos = []
    linhas_invalidas = 0
    with caminho.open("r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, 1):
            linha = linha.rstrip("\n")
            if not linha.strip():
                continue
            encontrado = PADRAO.fullmatch(linha)
            if not encontrado:
                linhas_invalidas += 1
                continue
            nivel = encontrado.group("nivel")
            contagem[nivel] += 1
            if nivel in ("ERROR", "CRITICAL"):
                eventos_criticos.append({
                    "linha": numero,
                    "data": encontrado.group("data"),
                    "nivel": nivel,
                    "mensagem": encontrado.group("mensagem"),
                })
    return {
        "arquivo": caminho.name,
        "total_eventos_validos": sum(contagem.values()),
        "por_nivel": {nivel: contagem[nivel] for nivel in NIVEIS},
        "linhas_invalidas": linhas_invalidas,
        "eventos_para_investigar": eventos_criticos,
        "situacao": "ATENCAO" if eventos_criticos else "NORMAL",
    }


def main():
    parser = argparse.ArgumentParser(description="Analisa logs fictícios de laboratório.")
    parser.add_argument(
        "arquivo", nargs="?", type=Path,
        default=Path(__file__).resolve().parents[1] / "exemplos/logs/servico-demo.log",
        help="Caminho para log de demonstração ou outro log autorizado.",
    )
    args = parser.parse_args()
    try:
        relatorio = analisar(args.arquivo)
    except (OSError, UnicodeError) as erro:
        parser.exit(2, f"Erro ao ler log: {erro}\n")
    print(json.dumps(relatorio, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
