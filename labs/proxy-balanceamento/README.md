# Nginx e HAProxy — Proxy reverso e balanceamento
Dois backends Nginx fictícios, HAProxy com round-robin e Nginx na entrada como proxy reverso. A porta de entrada fica restrita ao loopback. Execute:
```sh
docker compose up -d
bash testar.sh
docker compose down
```
O teste verifica ambos os backends e a continuidade após parar um deles. Diagnóstico: docker compose ps, logs, nginx -t, haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg. O ambiente não oferece TLS, autenticação ou HA do próprio balanceador. Em produção, valide esses requisitos e configure timeouts e observabilidade.