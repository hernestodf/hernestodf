# Plano de endereçamento e segmentação

O plano está no arquivo [rede.json](../rede.json), com três VLANs fictícias. Usamos endereços IPv4 reservados para documentação conforme RFC 5737.

| VLAN | Segmento | Rede | Gateway |
|---|---|---|---|
| 10 | Gestão | 192.0.2.0/27 | 192.0.2.1 |
| 20 | Usuários | 192.0.2.32/27 | 192.0.2.33 |
| 30 | Serviços | 192.0.2.64/27 | 192.0.2.65 |

Cada /27 tem 32 endereços, com 30 hosts utilizáveis. A segmentação entre VLANs depende de switches, roteamento e políticas de firewall adequados; declarar uma VLAN no papel não a implementa.

## Boas práticas

- Manter redes de gestão separadas das redes de usuários.
- Permitir somente fluxos necessários entre segmentos.
- Documentar gateway, DNS, DHCP e responsáveis por cada mudança.
- Testar alterações em ambiente autorizado e manter plano de reversão.
