#!/usr/bin/env python3
"""Valida plano IP fictício sem conectar à rede."""
import ipaddress
import json
import sys
from pathlib import Path

BLOCOS_DOCUMENTACAO = tuple(ipaddress.ip_network(x) for x in (
    "192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24"
))


def validar(plano):
    erros = []
    redes = []
    ids = set()
    vlans = plano.get("vlans")
    if not isinstance(vlans, list) or not vlans:
        return ["O plano precisa conter uma lista não vazia de VLANs."]
    for pos, vlan in enumerate(vlans, 1):
        if not isinstance(vlan, dict):
            erros.append(f"Entrada {pos}: VLAN inválida.")
            continue
        ident = vlan.get("id")
        if type(ident) is not int or not 1 <= ident <= 4094:
            erros.append(f"Entrada {pos}: identificador VLAN inválido.")
        elif ident in ids:
            erros.append(f"VLAN {ident}: identificador duplicado.")
        else:
            ids.add(ident)
        try:
            rede = ipaddress.ip_network(vlan["rede"], strict=True)
            gateway = ipaddress.ip_address(vlan["gateway"])
            if rede.version != 4 or not any(rede.subnet_of(b) for b in BLOCOS_DOCUMENTACAO):
                erros.append(f"VLAN {ident}: rede fora das faixas IPv4 de documentação.")
            if gateway not in rede.hosts():
                erros.append(f"VLAN {ident}: gateway não é endereço de host válido.")
            for anterior in redes:
                if rede.overlaps(anterior):
                    erros.append(f"VLAN {ident}: sub-rede sobreposta.")
            redes.append(rede)
        except (KeyError, ValueError, TypeError) as exc:
            erros.append(f"VLAN {ident}: endereço inválido ({exc}).")
    return erros


def main():
    caminho = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "rede.json"
    try:
        plano = json.loads(caminho.read_text(encoding="utf-8"))
        erros = validar(plano)
    except (OSError, ValueError, TypeError) as exc:
        print(f"Erro ao carregar plano: {exc}", file=sys.stderr)
        return 2
    if erros:
        for erro in erros:
            print(f"ERRO: {erro}", file=sys.stderr)
        return 1
    print(f"Plano fictício validado: {len(plano['vlans'])} VLANs, sem sobreposições.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
