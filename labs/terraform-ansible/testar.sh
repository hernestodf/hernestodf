#!/usr/bin/env bash
set -euo pipefail
export ANSIBLE_NOCOLOR=1
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
cp main.tf playbook.yml "$tmp/"
cd "$tmp"
terraform init -input=false
terraform validate
terraform plan -input=false -out=demo.tfplan
terraform apply -input=false demo.tfplan
terraform output -json configuracao > vars.json
ansible-playbook -i localhost, playbook.yml -e @vars.json -e "demo_dir=$tmp"
ansible-playbook -i localhost, playbook.yml -e @vars.json -e "demo_dir=$tmp" -e '{"verificar_idempotencia":true}'
grep -qx 'servico=portal-demo' servico.conf
grep -qx 'ambiente=laboratorio' servico.conf
terraform plan -input=false -detailed-exitcode
terraform destroy -auto-approve -input=false
