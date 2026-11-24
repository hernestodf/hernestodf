# RabbitMQ e Redis — Mensageria e cache
RabbitMQ desacopla produtores e consumidores; Redis fornece acesso rápido a valores temporários. O laboratório usa HTTP API de gerenciamento para publicar e consumir mensagem fictícia (ack de demonstração), redis-cli para testar TTL. Não usa cliente AMQP nem comprova entrega exatamente uma vez.
```sh
docker compose up -d
python3 testar.py
docker compose down -v
```
Porta de gerenciamento restrita ao loopback, credenciais apenas didáticas. Em produção use TLS, segredos, vhosts/ACL, confirmação de publicação, acknowledgements após processamento, DLQ, idempotência e política de expiração. Nunca armazene senhas em cache sem proteção.