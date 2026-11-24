import unittest
from validar import validar
class TestPlano(unittest.TestCase):
    def test_valido(self):
        self.assertEqual(validar({'ram_disponivel_mib':4096,'instancias':[{'id':100,'ram_mib':1024}]}),1024)
    def test_capacidade(self):
        with self.assertRaises(ValueError):
            validar({'ram_disponivel_mib':512,'instancias':[{'id':100,'ram_mib':1024}]})
    def test_duplicado(self):
        with self.assertRaises(ValueError):
            validar({'ram_disponivel_mib':4096,'instancias':[{'id':100,'ram_mib':1024}]*2})
