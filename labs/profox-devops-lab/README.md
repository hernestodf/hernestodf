# ProFox DevOps Lab

Laboratório **independente e fictício** de infraestrutura e CI/CD para portfólio. Não contém configurações de clientes ou ambientes de produção.

## O que demonstra
- API HTTP simples em Go com `/healthz` e `/readyz`
- Docker multi-stage e Compose
- Pipeline GitHub Actions com testes e build
- Health check e execução sem privilégios

## Executar
```bash
cd labs/profox-devops-lab
docker compose up --build -d
curl -f http://localhost:8088/healthz
docker compose down
```

Sem Docker: `go run ./cmd/server` (porta padrão 8080). Use `PORT=8088` para alterar.

## Arquitetura
```
cmd/server/main.go
Dockerfile
compose.yaml
.github/workflows/ci.yml
```

> Demonstração técnica. Não é uma configuração de deploy real da ProFox ou do SISLOC.
