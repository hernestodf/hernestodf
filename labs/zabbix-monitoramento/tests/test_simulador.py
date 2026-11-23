import unittest
from simulador import estado_alerta

class TestAlerta(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(estado_alerta([True, True]), "OK")
    def test_falha(self):
        self.assertEqual(estado_alerta([True, False, False, False]), "PROBLEMA")
    def test_recuperacao(self):
        self.assertEqual(estado_alerta([False, False, False, True]), "OK")
    def test_falha_transitoria(self):
        self.assertEqual(estado_alerta([False, False]), "OK")
    def test_limite_invalido(self):
        with self.assertRaises(ValueError):
            estado_alerta([], 0)
    def test_amostra_invalida(self):
        with self.assertRaises(ValueError):
            estado_alerta([1])
