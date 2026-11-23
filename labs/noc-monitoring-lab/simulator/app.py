"""Exportador Prometheus e simulador de incidentes fictícios (somente laboratório)."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock
from urllib.parse import parse_qs, urlsplit
import json

SCENARIOS = {
    "healthy": {"up": 1, "latency": 0.05, "errors": 0.0},
    "down": {"up": 0, "latency": 0.0, "errors": 1.0},
    "latency": {"up": 1, "latency": 1.5, "errors": 0.0},
    "errors": {"up": 1, "latency": 0.2, "errors": 0.25},
}
state = {"scenario": "healthy"}
lock = Lock()


def metrics(scenario):
    values = SCENARIOS[scenario]
    return (
        "# HELP noc_demo_service_up Logical health of the simulated service.\n"
        "# TYPE noc_demo_service_up gauge\n"
        f"noc_demo_service_up {values['up']}\n"
        "# HELP noc_demo_latency_seconds Simulated response latency in seconds.\n"
        "# TYPE noc_demo_latency_seconds gauge\n"
        f"noc_demo_latency_seconds {values['latency']}\n"
        "# HELP noc_demo_error_ratio Simulated error ratio from 0 to 1.\n"
        "# TYPE noc_demo_error_ratio gauge\n"
        f"noc_demo_error_ratio {values['errors']}\n"
    )


class Handler(BaseHTTPRequestHandler):
    def respond(self, code, body, content_type="application/json; charset=utf-8"):
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/healthz":
            self.respond(200, '{"status":"ok"}\n')
        elif path == "/metrics":
            with lock:
                scenario = state["scenario"]
            self.respond(200, metrics(scenario), "text/plain; version=0.0.4; charset=utf-8")
        elif path == "/state":
            with lock:
                scenario = state["scenario"]
            self.respond(200, json.dumps({"scenario": scenario}) + "\n")
        else:
            self.respond(404, '{"error":"not found"}\n')

    def do_POST(self):
        parsed = urlsplit(self.path)
        if parsed.path != "/simulate":
            self.respond(404, '{"error":"not found"}\\n')
            return
        scenario = parse_qs(parsed.query).get("scenario", [""])[0]
        if scenario not in SCENARIOS:
            self.respond(400, '{"error":"invalid scenario"}\n')
            return
        with lock:
            state["scenario"] = scenario
        self.respond(200, json.dumps({"scenario": scenario}) + "\n")


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
