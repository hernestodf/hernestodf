# Keycloak — IAM, OAuth 2.0 e OpenID Connect
Realm fictício com cliente confidencial de serviço. O exercício testa descoberta OIDC, token client_credentials e recusa de segredo incorreto. Não é fluxo de login humano nem demonstra SSO interativo: para isso, configure dois aplicativos de teste com Authorization Code + PKCE.
```sh
docker compose up -d
python3 testar.py
docker compose down -v
```
start-dev e segredos fictícios são exclusivos do laboratório. Produção exige HTTPS, banco persistente protegido, rotação de segredos, backup, configuração de hostname, validação de assinatura/issuer/audience/expiração do token no recurso protegido e menor privilégio.