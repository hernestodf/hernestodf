# INC-LINUX-001 — Disco quase cheio (simulação)

> **CASO INTEIRAMENTE FICTÍCIO.** Nenhum disco real foi preenchido e nenhuma empresa foi afetada.

| Campo | Exemplo didático |
|---|---|
| Prioridade | P3 — Média |
| Serviço | Aplicação de demonstração |
| Volume | `/dados-demo` (fictício) |
| Uso reportado | 93% (valor inventado) |
| Impacto | Risco hipotético de falha na gravação de logs |
| Situação | Resolvido (somente documentação do exercício) |

## Linha do tempo hipotética

- 09:00 — Alerta de ocupação de disco acima do limite didático.
- 09:05 — Analista reconhece e abre chamado.
- 09:10 — Consulta `df -h`, `df -i` e consumo de diretórios.
- 09:20 — Identifica retenção excessiva de arquivos fictícios como hipótese.
- 09:30 — Escalona para validação de política de retenção.
- 09:45 — Equipe aprova arquivamento fictício.
- 10:00 — Validação hipotética de recuperação.

## Diagnóstico e causa raiz

**Hipótese do exercício:** arquivos de log de demonstração acumulados por ausência de política de retenção. Esta causa é inventada, não foi observada em servidor real.

## Ações propostas

1. Revisar política de retenção e rotação de logs.
2. Criar alerta preventivo em limite inferior.
3. Validar periodicamente espaço e inodes.
4. Documentar responsáveis por expansão de armazenamento.

## Critérios de encerramento

Espaço e inodes dentro de limites aprovados, serviços funcionando e registro da investigação concluído.

[Consultar runbook](../docs/runbook-disco.md)
