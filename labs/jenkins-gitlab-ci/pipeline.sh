#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m unittest -v
mkdir -p dist
python3 -m zipfile -c dist/app.zip app.py
python3 -m zipfile -t dist/app.zip
