"""Testes HTTP reais do simulador em servidor local efêmero."""
import importlib.util
from pathlib import Path
from threading import Thread
from http.server import ThreadingHTTPServer
import json
import unittest
import urllib.error
import urllib.request

spec = importlib.util.spec_from_file_location("noc_app", Path(__file__).resolve().parents[1] / "app.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class HTTPTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def setUp(self):
        self.post("healthy")

    def post(self, scenario):
        request = urllib.request.Request(self.base + "/simulate?scenario=" + scenario, data=b"", method="POST")
        return urllib.request.urlopen(request, timeout=3)

    def test_health_and_metrics(self):
        with urllib.request.urlopen(self.base + "/healthz", timeout=3) as response:
            self.assertEqual(json.load(response)["status"], "ok")
        with urllib.request.urlopen(self.base + "/metrics", timeout=3) as response:
            self.assertIn("noc_demo_service_up 1", response.read().decode())

    def test_scenario_transitions(self):
        for scenario, expected in [("down", "noc_demo_service_up 0"), ("latency", "noc_demo_latency_seconds 1.5"), ("errors", "noc_demo_error_ratio 0.25")]:
            with self.subTest(scenario=scenario):
                with self.post(scenario) as response:
                    self.assertEqual(json.load(response)["scenario"], scenario)
                with urllib.request.urlopen(self.base + "/metrics", timeout=3) as response:
                    self.assertIn(expected, response.read().decode())

    def test_invalid_scenario(self):
        with self.assertRaises(urllib.error.HTTPError) as err:
            self.post("unknown")
        self.assertEqual(err.exception.code, 400)

    def test_unknown_route(self):
        with self.assertRaises(urllib.error.HTTPError) as err:
            urllib.request.urlopen(self.base + "/unknown", timeout=3)
        self.assertEqual(err.exception.code, 404)
