# Backup e Disaster Recovery

RPO é a perda de dados tolerável expressa em tempo; RTO é o prazo alvo de recuperação. Backup só tem valor comprovado quando uma restauração é testada.

## Prática local
```sh
python3 -m unittest -v
python3 recuperar.py
```
O script cria arquivos fictícios em diretório temporário, gera backup ZIP, calcula SHA-256 e restaura em outro diretório. Verifica integridade e rejeita caminhos perigosos, links e arquivos adulterados. A demonstração remove apenas os próprios temporários.

## Runbook
Declare incidente, isole o recurso afetado, preserve evidências, selecione backup íntegro, restaure em destino separado, valide conteúdo e aplicação e documente RPO/RTO observados. Em produção, use cópia externa, criptografia, retenção, controle de acesso, testes periódicos e estratégia 3-2-1. Hash sem assinatura não protege contra adulteração conjunta do backup e do hash. O lab não comprova recuperação de banco ou de infraestrutura inteira.
