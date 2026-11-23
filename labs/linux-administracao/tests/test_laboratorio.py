"""Testes seguros: executam scripts somente em dados temporários fictícios."""
import pathlib
import subprocess
import unittest

BASE = pathlib.Path(__file__).resolve().parents[1]


class LaboratorioLinuxTests(unittest.TestCase):
    def executar(self, nome):
        return subprocess.run(
            ["bash", str(BASE / "scripts" / nome)],
            capture_output=True, text=True, timeout=30, check=False
        )

    def test_backup_e_restauracao(self):
        resultado = self.executar("backup-demo.sh")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("validados com sucesso", resultado.stdout)

    def test_diagnostico_somente_leitura(self):
        resultado = self.executar("diagnostico.sh")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Nenhuma configuração foi modificada", resultado.stdout)
        self.assertIn("Uso de disco", resultado.stdout)

    def test_scripts_com_sintaxe_valida(self):
        for script in sorted((BASE / "scripts").glob("*.sh")):
            with self.subTest(script=script.name):
                resultado = subprocess.run(
                    ["bash", "-n", str(script)], capture_output=True, text=True
                )
                self.assertEqual(resultado.returncode, 0, resultado.stderr)


if __name__ == "__main__":
    unittest.main()
