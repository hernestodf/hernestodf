# Runbook: taxa de erros elevada (simulada)

**Alerta:** `DemoHighErrorRate` · **Severidade:** warning · **Condição:** `noc_demo_error_ratio > 0.1` por 30 s.

1. Consulte `noc_demo_error_ratio` no Prometheus.
2. Verifique se `noc_demo_service_up` também caiu; se sim, priorize o incidente de indisponibilidade.
3. Examine os logs do simulador: `docker compose logs --tail=100 simulator`.
4. Registre percentual, início e impacto hipotético; não atribua a falha a sistemas reais.
5. Recupere: `curl -X POST 'http://127.0.0.1:8000/simulate?scenario=healthy'`.
6. Confirme taxa de erros 0 e resolução do alerta.
