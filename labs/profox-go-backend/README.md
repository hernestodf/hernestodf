# ProFox Go Backend — API de tarefas

Projeto **demonstrativo, independente e com dados fictícios** para mostrar backend Go, PostgreSQL e práticas de API REST.

## Tecnologias
- Go 1.23, `net/http` e `database/sql`
- PostgreSQL com driver `pgx/v5/stdlib`
- SQL explícito, sem ORM
- Testes HTTP com `httptest`

## Endpoints
| Método | Rota | Resultado |
|---|---|---|
| GET | /healthz | Saúde da API |
| GET | /tasks | Lista tarefas |
| POST | /tasks | Cria tarefa (`{"title":"Revisar backup"}`) |

## Iniciar
```bash
cd labs/profox-go-backend
docker compose up --build -d
curl http://localhost:8090/healthz
curl -X POST http://localhost:8090/tasks -H 'Content-Type: application/json' -d '{"title":"Revisar backup"}'
curl http://localhost:8090/tasks
```

O banco é inicializado pelo script `db/init.sql` apenas na primeira criação do volume. Para reiniciar os dados de demonstração: `docker compose down -v`.

> Projeto educacional. Antes de usar em produção: autenticação, migrations versionadas, paginação, observabilidade e limites de requisição.
