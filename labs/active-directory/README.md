# Laboratório Active Directory e PowerShell

Projeto didático com dados exclusivamente fictícios. Não é uma implantação validada em produção.

## Exercício em Windows Server isolado
Use uma VM Windows Server de avaliação devidamente licenciada, com snapshot e rede interna isolada. Configure AD DS e DNS para o domínio fictício corp.example.test. Crie OUs TI e Operacoes, grupos de segurança e usuários fictícios. Vincule uma GPO de bloqueio de tela à OU de teste e valide com gpresult /r. Não conecte o laboratório a um domínio empresarial.

## Diagnóstico
Com o módulo ActiveDirectory instalado e acesso autorizado, consulte Get-ADUser, Get-ADGroup, Get-ADOrganizationalUnit e Get-ADDefaultDomainPasswordPolicy. Use Resolve-DnsName para verificar DNS e gpresult /r para políticas aplicadas. Não publique saídas reais.

O script abaixo valida um inventário fictício offline; não cria contas nem aplica GPOs.

## Testes locais

Execute na pasta do laboratório:

```sh
pwsh -NoProfile -File testar.ps1
```

O GitHub Actions verifica somente os scripts offline; a execução em infraestrutura real requer validação separada.
