import json
from pathlib import Path
import unittest
from auditar import auditar

class TestAuditoria(unittest.TestCase):
    def test_inventario(self):
        dados = json.loads(Path(__file__).with_name("inventario.json").read_text())
        self.assertEqual({a["risco"] for a in auditar(dados)}, {"MFA_AUSENTE", "REVISAR_PRIVILEGIO", "ARMAZENAMENTO_PUBLICO", "ADMINISTRACAO_ABERTA"})
    def test_vazio(self):
        self.assertEqual(auditar({"usuarios": [], "recursos": []}), [])
    def test_usuario_protegido(self):
        self.assertEqual(auditar({"usuarios": [{"login": "demo@example.test", "mfa": True, "admin": False}], "recursos": []}), [])
    def test_recurso_protegido(self):
        self.assertEqual(auditar({"usuarios": [], "recursos": [{"nome": "demo", "armazenamento_publico": False, "administracao_aberta": False}]}), [])
