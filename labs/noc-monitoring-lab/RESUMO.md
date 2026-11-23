# Resumo do projeto — Laboratório de Monitoramento NOC

## Visão geral

Laboratório prático e independente para demonstrar atividades de **Analista NOC, Suporte N2 e Infraestrutura**, incluindo monitoramento, identificação de falhas, análise de alertas, diagnóstico, recuperação de serviços e documentação de incidentes.

O projeto utiliza **dados totalmente fictícios** e não se conecta a ambientes empresariais.

## Tecnologias utilizadas

- **Prometheus:** coleta de métricas e regras de alerta.
- **Grafana:** visualização de disponibilidade, latência e taxa de erros.
- **Alertmanager:** recebimento e agrupamento de alertas simulados.
- **Python:** serviço HTTP que simula situações operacionais.
- **Docker Compose:** execução dos serviços em contêineres.
- **GitHub Actions:** testes automatizados e validação da aplicação.

## O que o laboratório demonstra

1. Monitoramento da disponibilidade de um serviço.
2. Simulação de indisponibilidade, lentidão e aumento de erros.
3. Identificação e classificação de incidentes por severidade.
4. Investigação com métricas, alertas e logs.
5. Recuperação e validação do retorno à normalidade.
6. Registro de incidentes, procedimentos operacionais e análise de causa raiz (RCA).
7. Automação de testes, validações de configuração e execução de um teste de recuperação no Docker.

## Competências aplicadas

**Operações NOC:** observabilidade, triagem de alertas, análise de incidentes, prioridades, SLA e escalonamento.

**Infraestrutura:** Linux, Docker, monitoramento de serviços e diagnóstico de problemas.

**Desenvolvimento e automação:** Python, HTTP, testes automatizados, GitHub Actions e integração contínua.

## Resultados verificáveis

O repositório contém código-fonte, configurações de monitoramento, regras de alerta, guias operacionais, um incidente fictício documentado, uma análise de causa raiz, diagrama de arquitetura e testes automatizados.

**Limitação importante:** o pipeline comprova os testes e a execução do simulador em contêiner; capturas reais dos painéis e uma demonstração visual completa dos alertas ainda dependem da execução manual do ambiente.

## Links

- [Código e instruções do laboratório](README.md)
- [Diagrama de arquitetura](docs/architecture.svg)
- [Apresentação para recrutadores](docs/portfolio-presentation.md)
- [Incidente fictício documentado](incidents/INC-2026-001.md)
- [Análise de causa raiz](incidents/RCA-2026-001.md)
- [Guias operacionais](runbooks/service-down.md)

---

**Resumo para currículo ou LinkedIn:** Desenvolvi um laboratório de monitoramento NOC com Prometheus, Grafana, Alertmanager, Python e Docker Compose, simulando incidentes de disponibilidade, latência e erros. Implementei alertas, procedimentos de diagnóstico e recuperação, documentação de incidentes e testes automatizados com GitHub Actions.
