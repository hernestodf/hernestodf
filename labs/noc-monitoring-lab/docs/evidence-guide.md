# Guia de evidências visuais do laboratório

Este documento orienta a captura de **imagens reais** do laboratório. Não substitua evidências por telas fictícias.

## Preparar

```bash
cd labs/noc-monitoring-lab
cp .env.example .env
# Altere GRAFANA_ADMIN_PASSWORD no .env
docker compose up --build -d
docker compose ps
```

Acesse apenas em seu próprio computador:
- Grafana: http://127.0.0.1:3000
- Prometheus Targets: http://127.0.0.1:9090/targets
- Prometheus Alerts: http://127.0.0.1:9090/alerts
- Alertmanager: http://127.0.0.1:9093

## Capturas recomendadas

| Arquivo sugerido | Tela | Critério |
|---|---|---|
| `screenshots/01-grafana-healthy.png` | Grafana / NOC Lab / Visão Geral | Disponibilidade 1, latência 0,05, erros 0 |
| `screenshots/02-prometheus-targets.png` | Prometheus /targets | Job `noc-demo-simulator` com estado UP |
| `screenshots/03-alert-firing.png` | Prometheus /alerts | `DemoServiceDown` em firing |
| `screenshots/04-alertmanager.png` | Alertmanager | Alerta de demonstração recebido |
| `screenshots/05-recovery.png` | Grafana após recuperar | Disponibilidade volta a 1 |

### Passo a passo da falha

```bash
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=down'
```

Aguarde pelo menos 60 segundos, confira a regra em firing e capture as telas. Depois:

```bash
curl -fsS -X POST 'http://127.0.0.1:8000/simulate?scenario=healthy'
```

Aguarde a resolução do alerta e capture a recuperação.

## Antes de publicar

- Não inclua credenciais, cookies, tokens, nomes de máquinas reais ou dados de terceiros.
- Prefira capturas apenas das páginas do laboratório, sem abas pessoais do navegador.
- Confirme que o timestamp da captura corresponde à execução mostrada.
- Adicione as imagens reais à pasta `screenshots/` e só então inclua-as no README.

## Galeria

**Capturas reais ainda não publicadas.** O diagrama de arquitetura em [architecture.svg](architecture.svg) é uma ilustração técnica, não uma captura do ambiente em execução.
