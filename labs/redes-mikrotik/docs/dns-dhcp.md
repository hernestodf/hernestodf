# DNS e DHCP: perguntas de suporte

## DNS

**Sintoma:** um serviço é acessível por IP, mas não por nome. Investigue o resolvedor configurado, cache, registros e alcance do servidor DNS. O comando `getent hosts localhost` é um teste local, não comprova que o DNS externo funciona.

## DHCP

**Sintoma:** estação não recebe configuração IPv4 esperada. Verifique interface, escopo, VLAN, relay DHCP, leases e disponibilidade do servidor. Um endereço automático de link local pode indicar falha na obtenção de lease.

## Caso fictício

Na VLAN 20, uma estação simulada recebe endereço e gateway, mas o resolvedor configurado está incorreto. A ação didática é revisar a opção DNS do escopo DHCP **em um ambiente de testes**, e validar nova concessão e resolução.

Não publique leases reais ou registros DNS internos.
