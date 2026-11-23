# NOC Monitoring Lab

Laboratório público e **100% fictício** para demonstrar monitoramento de serviços, alertas, investigação de incidentes e runbooks de operação NOC.

**Stack:** Prometheus, Alertmanager, Grafana, Python (stdlib), Docker Compose, testes `unittest` e GitHub Actions.

## Arquitetura

```text
[simulador HTTP /metrics] --scrape--> [Prometheus] --regras--> [Alertmanager]
                                              |
                                              +--> [Grafana dashboard]
```

- **Prometheus:** http://localhost:9090
- **Alertmanager:** http://localhost:9093
- **Grafana:** http://localhost:3000 (usuário `admin`; senha definida por `GRAFANA_ADMIN_PASSWORD`)
- **Simulador:** http://localhost:8000 (somente loopback)

Os alertas são internos ao laboratório; **não há envio de e-mail, SMS, Telegram ou WhatsApp**.

## Pré-requisitos

Docker Engine com plugin Compose. Este laboratório não usa endpoints, senhas ou dados de empresas reais.

## Início rápido

```bash
cd labs/noc-monitoring-lab
cp .env.example .env
# Edite .env e defina uma senha exclusiva para o Grafana.
docker compose up --build -d
docker compose ps
curl -fsS http://127.0.0.1:8000/healthz
curl -fsS http://127.0.0.1:8000/metrics
```

Abra o dashboard **NOC Lab / Visão Geral** no Grafana. O provisionamento do datasource e dashboard é automático.

## Simular incidentes

O simulador começa com serviço saudável, latência de 50 ms e zero erros.

```bash
# Incidente 1: indisponibilidade lógica do serviço (métrica passa a 0)
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=down'

# Incidente 2: latência elevada (1,5 segundo, valor simulado)
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=latency'

# Incidente 3: aumento da taxa de erros (25%, valor simulado)
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=errors'

# Recuperar serviço
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=healthy'
```

Aguarde o intervalo de coleta (15 s) e o período `for` das regras (30 s). Veja os alertas em http://localhost:9090/alerts e http://localhost:9093.

**Importante:** o cenário `down` simula falha de negócio por meio de uma métrica. Ele não derruba o container nem o endpoint `/metrics`; assim, a telemetria continua disponível para análise.

## Runbooks

- [Serviço indisponível](runbooks/service-down.md)
- [Latência elevada](runbooks/high-latency.md)
- [Taxa de erros elevada](runbooks/high-error-rate.md)

## Testes e validação

```bash
python3 -m unittest discover -s simulator/tests -v
docker compose config -q
docker compose run --rm --no-deps prometheus promtool check rules /etc/prometheus/alerts.yml
docker compose run --rm --no-deps prometheus promtool check config /etc/prometheus/prometheus.yml
```

No CI, os testes Python e a validação de configuração são executados automaticamente. Um teste de integração do ambiente Docker em execução pode ser feito manualmente com os comandos acima.

## Segurança e limites

- Portas publicadas **somente em 127.0.0.1**, não expostas à rede externa.
- `POST /simulate` **não possui autenticação** e é destinado exclusivamente ao ambiente local.
- Credenciais de exemplo não são adequadas para produção; altere a senha em `.env`.
- Sem serviços empresariais reais, sem webhook externo e sem dados pessoais.
- Imagens de terceiros têm tags de versão; para produção, use digests imutáveis, hardening adicional e políticas de atualização.
- Para encerrar: `docker compose down`. Para apagar os volumes do laboratório: `docker compose down -v`.

**Objetivo do portfólio:** demonstrar raciocínio de NOC, SRE básico, observabilidade, análise de incidentes e documentação operacional.
