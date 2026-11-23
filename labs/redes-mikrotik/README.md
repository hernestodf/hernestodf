# Laboratório de Redes e MikroTik — Suporte N2 e NOC

Projeto didático **100% fictício**, com topologia, endereçamento, diagnóstico de DNS, DHCP, VLAN, roteamento, VPN e exemplos de configuração RouterOS **para estudo, não para execução automática**.

**Objetivo profissional:** demonstrar troubleshooting de redes, documentação de infraestrutura, noções de segmentação, endereçamento IP e automação de validações com Python e GitHub Actions.

> **Segurança:** não há acesso a roteadores reais, credenciais, IPs de clientes ou equipamentos corporativos. Os exemplos RouterOS não são executados pelo CI. Revise com profissional autorizado antes de aplicar qualquer configuração em hardware.

## Topologia fictícia

```text
              [Internet simulada]
                      |
              [Roteador de borda]
                      |
                 [Switch VLAN]
              /       |        \
       VLAN 10     VLAN 20     VLAN 30
       Gestão      Usuários    Serviços
       .10.0/24    .20.0/24    .30.0/24
```

Todos os endereços pertencem à faixa de documentação **192.0.2.0/24, 198.51.100.0/24 ou 203.0.113.0/24**. A tabela do laboratório utiliza sub-redes /27 da primeira faixa; os rótulos acima são nomes lógicos, não endereços completos.

| VLAN | Finalidade | Sub-rede fictícia | Gateway ilustrativo |
|---|---|---|---|
| 10 | Gestão | 192.0.2.0/27 | 192.0.2.1 |
| 20 | Usuários | 192.0.2.32/27 | 192.0.2.33 |
| 30 | Serviços | 192.0.2.64/27 | 192.0.2.65 |

## Conteúdo

- [Plano de endereçamento e segmentação](docs/plano-de-rede.md)
- [Roteiro de troubleshooting de redes](docs/troubleshooting.md)
- [DNS e DHCP: diagnóstico e hipóteses](docs/dns-dhcp.md)
- [VPN e segurança: princípios](docs/vpn-seguranca.md)
- [Exemplo RouterOS — somente leitura e estudo](mikrotik/exemplo-routeros.rsc)
- [Incidente fictício de DNS](incidentes/INC-REDE-001.md)
- [Validador de plano IP](scripts/validar_rede.py)

## Executar testes

```bash
cd labs/redes-mikrotik
python3 scripts/validar_rede.py
python3 -m unittest discover -s tests -v
```

O validador usa somente a biblioteca padrão do Python e verifica sub-redes, gateways, conflitos de endereçamento, VLANs duplicadas e pertencimento aos blocos reservados para documentação.

## Evidências

O GitHub Actions verifica sintaxe Python, testes unitários e validação do plano de rede. **Não testa um roteador MikroTik físico, nem confirma comunicação real entre VLANs, VPN ou servidores DNS/DHCP.**

## Competências

TCP/IP · Sub-redes · VLAN · DNS · DHCP · Roteamento · MikroTik RouterOS · Troubleshooting · Segurança de rede · Python · CI/CD.

[Voltar ao perfil](../../README.md)
