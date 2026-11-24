import unittest
from pathlib import Path
import tempfile
import zipfile
from recuperar import backup, restaurar, hash_arquivo

class TestRecuperacao(unittest.TestCase):
    def test_restore(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p/"origem").mkdir()
            (p/"origem"/"a.txt").write_text("demo")
            h = backup(p/"origem", p/"b.zip")
            restaurar(p/"b.zip", p/"novo", h)
            self.assertEqual((p/"novo"/"a.txt").read_text(), "demo")
            with self.assertRaises(ValueError):
                restaurar(p/"b.zip", p/"novo", h)
    def test_hash(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p/"b.zip").write_bytes(b"alterado")
            with self.assertRaises(ValueError):
                restaurar(p/"b.zip", p/"novo", "0"*64)
            self.assertFalse((p/"novo").exists())
    def test_traversal(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            with zipfile.ZipFile(p/"b.zip","w") as z:
                z.writestr("../fora.txt","demo")
            with self.assertRaises(ValueError):
                restaurar(p/"b.zip", p/"novo", hash_arquivo(p/"b.zip"))
            self.assertFalse((p/"fora.txt").exists())
