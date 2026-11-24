#!/usr/bin/env bash
set -euo pipefail
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
docker run --rm -v "$PWD:/repo:ro" zricethezav/gitleaks:v8.24.3 dir /repo --redact --no-banner
docker run --rm -v "$PWD:/repo:ro" aquasec/trivy:0.62.1 config --severity HIGH,CRITICAL --exit-code 1 /repo
mkdir "$tmp/fixture"
printf 'FROM alpine:3.22\nUSER root\n' > "$tmp/fixture/Dockerfile"
docker run --rm -v "$tmp/fixture:/fixture:ro" aquasec/trivy:0.62.1 config --format json /fixture > "$tmp/report.json"
python3 - "$tmp/report.json" <<'PY'
import json,sys
r=json.load(open(sys.argv[1]))
assert any(m.get("Severity") in ("HIGH","CRITICAL") for x in r.get("Results",[]) for m in x.get("Misconfigurations",[])), "Fixture insegura nao detectada"
PY
