# Runbook — alerta de uso de disco (cenário fictício)

**Gatilho didático:** uso de disco acima de 90% em volume fictício.

1. **Reconhecer:** registrar o horário do alerta e a identificação do volume.
2. **Confirmar:** usar `df -h` e `df -i` para distinguir espaço de inodes.
3. **Investigar:** identificar diretórios maiores com `du -sh` e revisar política de logs.
4. **Avaliar impacto:** verificar se gravações, logs e serviços estão comprometidos.
5. **Escalonar:** se houver risco de indisponibilidade ou necessidade de exclusão/migração de dados, acionar responsável técnico.
6. **Recuperar:** aplicar somente ação aprovada (retenção, expansão de volume ou arquivamento).
7. **Validar:** confirmar espaço disponível e funcionamento dos serviços.
8. **Encerrar:** registrar causa raiz, evidências e prevenção.

**Não execute:** `rm -rf`, limpeza de logs, expansão de partição ou reinício de serviços em produção sem aprovação e plano de retorno.
