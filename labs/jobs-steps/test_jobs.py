import unittest
from jobs import Step, rodar

def falhar():
    raise RuntimeError("demo")

class TestJobs(unittest.TestCase):
    def test_ordem(self):
        ordem = []
        r = rodar([Step("b", lambda: ordem.append("b"), ("a",)), Step("a", lambda: ordem.append("a"))])
        self.assertEqual(ordem, ["a", "b"])
        self.assertEqual(r["b"]["estado"], "OK")
    def test_bloqueio(self):
        r = rodar([Step("a", falhar), Step("b", lambda: None, ("a",)), Step("c", lambda: None)])
        self.assertEqual(r["a"]["tentativas"], 2)
        self.assertEqual(r["b"]["estado"], "BLOQUEADO")
        self.assertEqual(r["c"]["estado"], "OK")
    def test_retry(self):
        n = []
        def executar():
            n.append(1)
            if len(n) == 1:
                falhar()
        self.assertEqual(rodar([Step("a", executar)])["a"], {"estado": "OK", "tentativas": 2})
    def test_ciclo(self):
        with self.assertRaises(ValueError):
            rodar([Step("a", lambda: None, ("b",)), Step("b", lambda: None, ("a",))])
    def test_dependencia(self):
        with self.assertRaises(ValueError):
            rodar([Step("a", lambda: None, ("x",))])
