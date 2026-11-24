# Laboratório Microsoft 365, Azure e AWS

Portfólio didático de suporte corporativo e infraestrutura cloud. Todos os dados são fictícios. Nenhuma API cloud é chamada, nenhum recurso é provisionado e nenhuma credencial é necessária.

## Exercícios
- [Microsoft 365 e Entra ID](docs/m365-entra.md)
- [Azure](docs/azure.md)
- [AWS](docs/aws.md)
- [Incidente simulado](docs/incidente.md)

## Demonstração executável
O inventário JSON representa usuários, licenças, MFA e recursos cloud. O auditor Python identifica ausência de MFA, privilégios administrativos, armazenamento público e regras administrativas abertas. O script PowerShell resume usuários e licenças offline.

```bash
python3 auditar.py
python3 -m unittest -v
pwsh -NoProfile -File inventario.ps1
```

O CI executa testes offline. Não comprova acesso ao Microsoft Graph, Azure ou AWS, nem implantação real. Os roteiros exigem tenant/conta de testes autorizados, controle de custos e validação separada.
