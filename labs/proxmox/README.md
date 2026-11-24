# Laboratório Proxmox VE e Virtualização

Projeto didático com dados exclusivamente fictícios. Não é uma implantação validada em produção.

## Exercício de virtualização
Em um host Proxmox de laboratório autorizado, crie uma VM Linux e um container LXC não privilegiado. Use rede interna isolada, sem acesso à infraestrutura empresarial. Documente CPU, memória, armazenamento e bridge. Faça backup com a interface do Proxmox, restaure com outro ID e valide inicialização e integridade. Snapshot não substitui backup independente.

## Diagnóstico
Comandos consultivos no host autorizado: pveversion, qm list, pct list, pvesm status. Não execute restauração sobre uma VM existente. O validador offline abaixo verifica capacidade planejada e IDs duplicados, não acessa a API Proxmox nem cria VMs.

## Testes locais

Execute na pasta do laboratório:

```sh
python3 -m unittest -v && python3 validar.py
```

O GitHub Actions verifica somente os scripts offline; a execução em infraestrutura real requer validação separada.
