import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("noc_simulator", Path(__file__).resolve().parents[1] / "app.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MetricsTest(unittest.TestCase):
    def test_healthy(self):
        result = module.metrics("healthy")
        self.assertIn("noc_demo_service_up 1", result)
        self.assertIn("noc_demo_error_ratio 0.0", result)

    def test_down(self):
        self.assertIn("noc_demo_service_up 0", module.metrics("down"))

    def test_latency(self):
        self.assertIn("noc_demo_latency_seconds 1.5", module.metrics("latency"))

    def test_errors(self):
        self.assertIn("noc_demo_error_ratio 0.25", module.metrics("errors"))

    def test_scenarios_are_distinct(self):
        self.assertEqual(set(module.SCENARIOS), {"healthy", "down", "latency", "errors"})


if __name__ == "__main__":
    unittest.main()
