# Laboratório de Hardening Linux

Projeto didático com dados exclusivamente fictícios. Não é uma implantação validada em produção.

## Auditoria de segurança
O auditor analisa uma configuração SSH fictícia e permissões de arquivos temporários. Não altera serviços, firewall ou contas. Em produção, verifique a configuração efetiva com sshd -T, incluindo blocos Match e arquivos Include; este parser didático não os interpreta.

## Roteiro operacional
Revise autenticação por chave, acesso root, atualizações, regras de firewall, Fail2ban, logs e backups. Antes de desativar senhas ou alterar SSH, valide acesso alternativo e mantenha uma sessão administrativa aberta. Teste mudanças em VM isolada, com rollback. Consulte ufw status verbose ou nft list ruleset somente com autorização.

## Testes locais

Execute na pasta do laboratório:

```sh
python3 -m unittest -v && python3 auditar.py
```

O GitHub Actions verifica somente os scripts offline; a execução em infraestrutura real requer validação separada.
