import unittest
from app import normalizar
class TestApp(unittest.TestCase):
    def test_normalizar(self):
        self.assertEqual(normalizar("  chamado   demo  "),"CHAMADO DEMO")
