# Loki e OpenTelemetry — Logs centralizados
Um OpenTelemetry Collector recebe logs OTLP/HTTP e exporta para Loki. O teste envia evento fictício e consulta LogQL até encontrá-lo. Sem credenciais reais e sem portas públicas.
```sh
docker compose up -d
python3 testar.py
docker compose down -v
```
Observe service.name, timestamp, severidade e corpo do evento. Em Loki, rótulos de baixa cardinalidade são preferíveis; IDs de requisições devem ser atributos/metadados, não rótulos de alta cardinalidade. OpenTelemetry padroniza coleta e exportação de telemetria; Loki armazena e consulta logs. Este exercício cobre logs, não tracing distribuído ou métricas OTLP. Em produção configure autenticação, TLS, retenção, armazenamento e proteção de dados.
