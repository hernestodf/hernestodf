import copy
import importlib.util
import json
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validar_rede", BASE / "scripts/validar_rede.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestPlanoRede(unittest.TestCase):
    def setUp(self):
        self.plano = json.loads((BASE / "rede.json").read_text(encoding="utf-8"))

    def test_plano_valido(self):
        self.assertEqual(MOD.validar(self.plano), [])

    def test_sobreposicao(self):
        plano = copy.deepcopy(self.plano)
        plano["vlans"][1]["rede"] = "192.0.2.0/28"
        plano["vlans"][1]["gateway"] = "192.0.2.2"
        self.assertTrue(any("sobreposta" in x for x in MOD.validar(plano)))

    def test_gateway_fora_da_rede(self):
        plano = copy.deepcopy(self.plano)
        plano["vlans"][0]["gateway"] = "192.0.2.50"
        self.assertTrue(any("gateway" in x for x in MOD.validar(plano)))

    def test_vlan_duplicada(self):
        plano = copy.deepcopy(self.plano)
        plano["vlans"][1]["id"] = 10
        self.assertTrue(any("duplicado" in x for x in MOD.validar(plano)))

    def test_ip_real_rejeitado(self):
        plano = copy.deepcopy(self.plano)
        plano["vlans"][0]["rede"] = "10.0.0.0/27"
        plano["vlans"][0]["gateway"] = "10.0.0.1"
        self.assertTrue(any("documentação" in x for x in MOD.validar(plano)))

    def test_lista_vazia(self):
        self.assertTrue(MOD.validar({"vlans": []}))

    def test_vlan_booleana_rejeitada(self):
        plano = copy.deepcopy(self.plano)
        plano["vlans"][0]["id"] = True
        self.assertTrue(any("inválido" in x for x in MOD.validar(plano)))


if __name__ == "__main__":
    unittest.main()
