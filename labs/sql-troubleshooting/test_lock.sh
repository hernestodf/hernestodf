#!/usr/bin/env bash
set -euo pipefail
psql_demo() { docker compose exec -T db psql -X -U demo -d demo -v ON_ERROR_STOP=1 "$@"; }
psql_demo -c "BEGIN; SELECT pg_advisory_xact_lock(12345); SELECT pg_sleep(8); COMMIT;" &
holder=$!
trap 'wait "$holder" || true' EXIT
ready=0
for i in $(seq 1 30); do
  if [[ "$(psql_demo -Atc "SELECT count(*) FROM pg_locks WHERE locktype='advisory' AND granted")" == 1 ]]; then ready=1; break; fi
  sleep 0.1
done
[[ "$ready" == 1 ]]
if output=$(psql_demo -c "SET lock_timeout='500ms'; SELECT pg_advisory_lock(12345);" 2>&1); then
  echo "Era esperado timeout"; exit 1
fi
grep -qi 'lock timeout' <<< "$output"
wait "$holder"
psql_demo -c "SELECT pg_advisory_lock(12345); SELECT pg_advisory_unlock(12345);"
