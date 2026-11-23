# Matriz didática de severidade, SLA e escalonamento

> Valores **fictícios**, criados exclusivamente para o NOC Monitoring Lab. Não representam SLAs de Sicoob, Stefanini, ProFox ou qualquer organização real.

| Prioridade | Exemplo | Reconhecimento-alvo | Recuperação-alvo | Escalonamento |
|---|---|---|---|---|
| P1 — Crítica | Indisponibilidade total com impacto amplo | 5 min | 30 min | Imediato para plantão técnico |
| P2 — Alta | Serviço indisponível para grupo relevante | 10 min | 60 min | Após 15 min sem recuperação |
| P3 — Média | Latência ou erros parciais | 30 min | 4 h | Após 60 min sem evolução |
| P4 — Baixa | Degradação sem impacto significativo | 4 h | 2 dias úteis | Próximo ciclo de atendimento |

## Processo de incidente

1. **Detectar:** receber alerta e confirmar a métrica.
2. **Classificar:** avaliar impacto e urgência hipotéticos.
3. **Reconhecer:** abrir chamado e registrar responsável e horários.
4. **Investigar:** usar dashboard, Prometheus, logs e runbook.
5. **Escalonar:** se ultrapassar gatilho ou exigir especialista.
6. **Recuperar:** executar ação segura e validar métricas.
7. **Encerrar:** registrar causa, duração, evidências e melhorias.

## Fórmulas

- **MTTA:** média dos tempos entre alerta e reconhecimento.
- **MTTR:** média dos tempos entre início do incidente e recuperação.
- **Disponibilidade:** tempo disponível dividido pelo tempo total observado.

Não calcular indicadores reais a partir da linha do tempo fictícia sem dados de observação.
