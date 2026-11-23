# Runbook: latência elevada (simulada)

**Alerta:** `DemoHighLatency` · **Severidade:** warning · **Condição:** `noc_demo_latency_seconds > 1` por 30 s.

1. Confira a série temporal no Grafana e a consulta no Prometheus.
2. Compare com a métrica `noc_demo_error_ratio` para identificar correlação.
3. Consulte `docker compose ps` e logs do simulador.
4. Registre início, duração, valor máximo e hipótese do incidente fictício.
5. Recupere: `curl -X POST 'http://127.0.0.1:8000/simulate?scenario=healthy'`.
6. Confirme latência retornando a 0,05 s e resolução do alerta.

**Nota:** a latência é um número simulado, não uma medição de requisições reais.
