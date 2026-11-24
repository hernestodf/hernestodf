import unittest
from datetime import datetime, timezone
from sla import avaliar
class TestSLA(unittest.TestCase):
    def test_aberto(self):
        c={"id":"demo","prioridade":"P1","aberto":"2026-01-01T09:00:00Z"}
        self.assertEqual(avaliar(c,datetime(2026,1,1,13,tzinfo=timezone.utc))["sla"],"NO_PRAZO")
        self.assertEqual(avaliar(c,datetime(2026,1,1,14,tzinfo=timezone.utc))["sla"],"VENCIDO")
    def test_datas(self):
        with self.assertRaises(ValueError):
            avaliar({"id":"demo","prioridade":"P1","aberto":"2026-01-01T09:00:00Z","resolvido":"2026-01-01T08:00:00Z"})
