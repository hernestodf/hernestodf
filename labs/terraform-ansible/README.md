# Terraform e Ansible — Infraestrutura como código

Terraform descreve o estado desejado de recursos; Ansible configura sistemas. Este exercício usa apenas recursos locais e um diretório temporário. Não há credenciais, APIs cloud, sudo ou máquinas externas.

## Prática
Instale Terraform >= 1.4 e Ansible Core. Na pasta do laboratório, execute bash testar.sh. Terraform cria um recurso terraform_data sem provider externo, exporta uma configuração JSON e Ansible configura um arquivo local. O segundo playbook comprova idempotência; terraform plan -detailed-exitcode verifica ausência de mudanças.

Em produção, use state remoto protegido, revisão de plano, separação de ambientes, secrets e inventários autorizados. Nunca comite state. O exercício não provisiona EC2, Azure VM nem servidores reais.
