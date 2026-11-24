import unittest
from auditar import auditar
class TestAuditoria(unittest.TestCase):
    def test_seguro(self):
        self.assertTrue(all(auditar('PermitRootLogin no\nPasswordAuthentication no', 0o600).values()))
    def test_inseguro(self):
        self.assertFalse(any(auditar('PermitRootLogin yes\nPasswordAuthentication yes', 0o644).values()))
    def test_ausente(self):
        self.assertFalse(auditar('', 0o600)['root_desativado'])
    def test_primeira_ocorrencia(self):
        self.assertFalse(auditar('PermitRootLogin yes\nPermitRootLogin no', 0o600)['root_desativado'])
