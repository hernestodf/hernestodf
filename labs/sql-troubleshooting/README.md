# SQL Troubleshooting — PostgreSQL

Banco descartável com registros fictícios. O exercício cria uma tabela, índice, carga e consultas; verifica transações e disputa de locks.

## Executar localmente
```sh
docker compose up -d --wait
docker compose exec -T db psql -U demo -d demo -v ON_ERROR_STOP=1 < laboratorio.sql
docker compose exec -T db psql -U demo -d demo -v ON_ERROR_STOP=1 < testes.sql
docker compose down -v
```
A última linha apaga apenas o volume deste laboratório. Não a use em bancos reais.

## Diagnóstico
EXPLAIN mostra o plano estimado; EXPLAIN ANALYZE executa a consulta. Compare leituras e plano antes/depois do índice; a escolha do índice depende do otimizador. pg_stat_activity mostra sessões, pg_locks mostra locks e pg_blocking_pids identifica bloqueadores. Locks são normais; contenção prolongada exige análise. Deadlock é um ciclo de espera; o PostgreSQL aborta uma transação para resolvê-lo. Não encerre sessões reais sem autorização.

O pipeline inicia PostgreSQL em container e testa consultas, rollback e lock_timeout em duas sessões. Não simula um deadlock real nem mede desempenho de produção.
