# Automação de Jobs e Steps

Simulador de processamento fictício, sem dependência de sistemas empresariais. Uma DAG representa dependências entre steps. Falhas transitórias podem ser repetidas até o limite; falhas definitivas bloqueiam dependentes, mas não ramos independentes.

## Executar
```sh
python3 jobs.py
python3 -m unittest -v
```

O exemplo simula extração, validação e consolidação de dados fictícios. Cada tentativa aparece no relatório JSON. Um ciclo ou dependência desconhecida é rejeitado antes de executar qualquer step.

## Runbook
Identifique o step que falhou, confira dependências e tentativas, preserve evidências e verifique se o processo é idempotente antes de reprocessar. Em produção, use estado persistente, locking, timeouts, retentativas com backoff, auditoria e autorização. Este executor em memória não garante processamento exatamente uma vez nem recuperação após reinício. O CI executa testes e a demonstração; não faz deploy.
