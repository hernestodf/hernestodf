# Análise de logs Linux — exercício de troubleshooting

Este exercício usa um log **inteiramente fictício** de serviço e um analisador em Python (biblioteca padrão). Não há acesso a servidores externos, dados pessoais ou sistemas empresariais.

## Executar

```bash
cd labs/linux-administracao
python3 scripts/analisar_logs.py
```

O resultado é um relatório JSON com quantidade de mensagens por severidade, linhas inválidas e eventos que merecem investigação.

## Cenário simulado

O arquivo `exemplos/logs/servico-demo.log` contém sete eventos: três INFO, um WARNING, dois ERROR e um CRITICAL. O objetivo é identificar erros de conexão fictícios e um evento de indisponibilidade, seguido por uma mensagem de recuperação.

## Como interpretar

1. Confirme a janela de tempo e a fonte do log.
2. Compare os erros com métricas de disponibilidade, memória e disco.
3. Procure repetição de mensagens e eventos próximos.
4. Registre hipótese, evidências e próximo passo.
5. Não confunda um log de recuperação com prova definitiva de que o serviço está saudável: valide o estado real e as métricas.

## Cuidados em ambientes reais

- Não publique logs com IPs internos, tokens, credenciais ou dados pessoais.
- Evite executar análises em logs sensíveis sem autorização.
- Faça a coleta e retenção conforme as políticas da organização.
- Este script é didático; não substitui SIEM, correlação de eventos ou monitoramento contínuo.
