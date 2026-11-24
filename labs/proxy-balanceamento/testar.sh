#!/usr/bin/env bash
set -euo pipefail
url=http://127.0.0.1:18081/
for i in $(seq 1 30); do
  if curl -fsS "$url" >/dev/null; then break; fi
  sleep 1
done
docker compose exec -T proxy nginx -t
docker compose exec -T balanceador haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg
res=$(for i in $(seq 1 12); do curl -fsS "$url"; done)
grep -qx backend-a <<< "$res"
grep -qx backend-b <<< "$res"
docker compose stop b
sleep 4
for i in $(seq 1 5); do
  [[ "$(curl -fsS "$url")" == backend-a ]]
done
docker compose start b
