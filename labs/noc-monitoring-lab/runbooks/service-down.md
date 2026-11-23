# Runbook: serviço indisponível (simulado)

**Alerta:** `DemoServiceDown` · **Severidade:** critical · **Métrica:** `noc_demo_service_up == 0` por 30 s.

1. **Confirmar:** abra Prometheus → Alerts e consulte `noc_demo_service_up`.
2. **Distinguir:** verifique `up{job="noc-demo-simulator"}`. Se for 1, o exporter está acessível e a falha é lógica/simulada; se for 0, investigue o scrape ou container.
3. **Inspecionar:** `docker compose ps`, `docker compose logs --tail=100 simulator`.
4. **Registrar:** horário, alerta, métrica, hipótese, impacto fictício e evidências.
5. **Recuperar:** `curl -X POST 'http://127.0.0.1:8000/simulate?scenario=healthy'`.
6. **Validar:** confirme métrica igual a 1 e alerta resolvido após novas avaliações.

**Escalonamento (exercício):** se a indisponibilidade persistir por mais de 10 minutos, registrar incidente e encaminhar ao responsável técnico fictício. Não utilizar contatos reais.
