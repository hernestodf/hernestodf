# Roteiro de troubleshooting de rede

Execute somente em máquinas ou redes autorizadas. Os comandos são **consultivos**.

| Etapa | Comando Linux | Interpretação |
|---|---|---|
| Interface | `ip -br addr` | Endereço e estado da interface |
| Rota | `ip route` | Gateway e rotas instaladas |
| DNS | `getent hosts localhost` | Resolução de nomes local |
| Portas | `ss -tuln` | Serviços em escuta |
| Configuração DNS | `cat /etc/resolv.conf` | Resolvedor configurado |
| Vizinhança | `ip neigh` | Cache de vizinhos |
| Logs | `journalctl -p warning -n 30` | Avisos recentes (systemd) |

## Fluxo de diagnóstico

1. Confirmar escopo: um usuário, uma VLAN ou toda a rede?
2. Verificar link, endereço IP, máscara, gateway e rota.
3. Diferenciar falha de DNS de falha de conectividade IP.
4. Conferir se DHCP entregou endereço e parâmetros esperados.
5. Examinar regras de segmentação e firewall **sem alterá-las**.
6. Documentar testes, horário, hipótese, evidências e escalonamento.

Não execute varreduras ou testes ativos em redes de terceiros sem autorização.
