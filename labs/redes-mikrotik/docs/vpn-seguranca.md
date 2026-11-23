# VPN, roteamento e segurança — princípios

- **VPN:** túnel autenticado e criptografado para acesso autorizado. Verifique rotas, DNS, políticas de acesso, certificados e logs.
- **Roteamento:** uma rota válida precisa de destino, próximo salto e conectividade. Use `ip route` para leitura no Linux.
- **VLAN:** segmentação de camada 2; não substitui firewall.
- **Firewall:** aplique menor privilégio, registre mudanças e tenha plano de reversão.
- **MikroTik:** preserve backup e exportação de configuração antes de mudanças autorizadas. Não exponha WinBox/SSH à Internet sem controles apropriados.

Este repositório não inclui credenciais, chaves VPN ou configurações prontas para implantação em produção.
