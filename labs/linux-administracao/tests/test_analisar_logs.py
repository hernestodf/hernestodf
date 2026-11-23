"""Testes do analisador usando apenas arquivos fictícios."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

BASE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("analisar_logs", BASE / "scripts/analisar_logs.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class TestAnalisarLogs(unittest.TestCase):
    def test_amostra_ficticia(self):
        r = MOD.analisar(BASE / "exemplos/logs/servico-demo.log")
        self.assertEqual(r["total_eventos_validos"], 7)
        self.assertEqual(r["por_nivel"]["ERROR"], 2)
        self.assertEqual(r["por_nivel"]["CRITICAL"], 1)
        self.assertEqual(len(r["eventos_para_investigar"]), 3)
        self.assertEqual(r["situacao"], "ATENCAO")

    def test_log_sem_erros(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "exemplo.log"
            caminho.write_text("2026-11-23T10:00:00Z INFO exemplo\n", encoding="utf-8")
            r = MOD.analisar(caminho)
            self.assertEqual(r["situacao"], "NORMAL")
            self.assertEqual(r["por_nivel"]["INFO"], 1)

    def test_linha_invalida(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "exemplo.log"
            caminho.write_text("texto inválido\n2026-11-23T10:00:00Z WARNING exemplo\n", encoding="utf-8")
            r = MOD.analisar(caminho)
            self.assertEqual(r["linhas_invalidas"], 1)
            self.assertEqual(r["total_eventos_validos"], 1)

    def test_arquivo_vazio(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "exemplo.log"
            caminho.write_text("", encoding="utf-8")
            r = MOD.analisar(caminho)
            self.assertEqual(r["total_eventos_validos"], 0)
            self.assertEqual(r["situacao"], "NORMAL")


if __name__ == "__main__":
    unittest.main()
