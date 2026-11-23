#!/usr/bin/env sh
set -eu
BASE="${BASE_URL:-http://127.0.0.1:8000}"
echo "Checking health endpoint..."
curl --fail --silent --show-error "$BASE/healthz" | grep -q '"status":"ok"'
echo "Checking healthy metrics..."
curl --fail --silent --show-error "$BASE/metrics" | grep -q 'noc_demo_service_up 1'
echo "Simulating down incident..."
curl --fail --silent --show-error -X POST "$BASE/simulate?scenario=down" >/dev/null
curl --fail --silent --show-error "$BASE/metrics" | grep -q 'noc_demo_service_up 0'
echo "Recovering..."
curl --fail --silent --show-error -X POST "$BASE/simulate?scenario=healthy" >/dev/null
curl --fail --silent --show-error "$BASE/metrics" | grep -q 'noc_demo_service_up 1'
echo "Smoke test passed."
