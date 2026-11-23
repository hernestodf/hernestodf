# Laboratório de Administração Linux e Diagnóstico de Problemas

Laboratório **100% fictício**, voltado a demonstrar competências de **Suporte N2, NOC e Administração Linux**: análise de serviços, recursos do sistema, permissões, rede, logs, backup e recuperação.

**Tecnologias:** Bash, Python 3 (biblioteca padrão), Docker, ShellCheck e GitHub Actions.

> **Segurança:** todos os exemplos utilizam nomes, usuários, IPs e arquivos de demonstração. Os scripts operam somente em arquivos temporários do laboratório, sem `sudo`, sem alterações de firewall, SSH, contas do sistema ou serviços reais.

## Arquitetura e atividades

| Atividade | Ferramentas | Evidência |
|---|---|---|
| Inventário básico do host | `uname`, `id`, `df`, `free` | `scripts/diagnostico.sh` |
| Diagnóstico de rede | `ip`, `getent`, `ping` (opcional) | `docs/roteiro-troubleshooting.md` |
| Diagnóstico de serviços e logs | `systemctl`, `journalctl` (somente leitura) | `docs/roteiro-troubleshooting.md` |
| Backup e recuperação | `tar`, `sha256sum`, `cmp` | `scripts/backup-demo.sh` |
| Verificação automatizada | `unittest`, `bash -n`, ShellCheck | GitHub Actions |

## Início rápido

Requisitos: Linux com Bash e ferramentas GNU básicas; Python 3 para testes. Docker é opcional.

```bash
git clone https://github.com/hernestodf/hernestodf.git
cd hernestodf/labs/linux-administracao

bash scripts/diagnostico.sh
bash scripts/backup-demo.sh
python3 -m unittest discover -s tests -v
```

O script de backup cria seu próprio diretório temporário, simula arquivos de configuração e logs, faz um arquivo `.tar.gz`, verifica o conteúdo e restaura em uma segunda pasta temporária. **Nenhum arquivo de produção é lido ou alterado.**

### Usando Docker (opcional)

```bash
docker build -t laboratorio-linux .
docker run --rm --network none --read-only --tmpfs /tmp:rw,nosuid,nodev --cap-drop ALL laboratorio-linux
```

A imagem executa somente a demonstração de backup. O contêiner não recebe acesso à rede ou ao host.

## Roteiros de incidentes fictícios

- [Diagnóstico de CPU, memória, disco, serviços e rede](docs/roteiro-troubleshooting.md)
- [Incidente fictício: disco quase cheio](incidentes/INC-LINUX-001.md)
- [Runbook de recuperação e escalonamento](docs/runbook-disco.md)
- [Comandos Linux para entrevistas técnicas](docs/comandos-essenciais.md)

## Testes e integração contínua

O fluxo do GitHub Actions executa validação de sintaxe Bash, ShellCheck, testes Python, a demonstração de backup, a construção da imagem Docker e a execução isolada do contêiner.

**Observação:** o laboratório não executa falhas reais no sistema operacional nem modifica serviços, discos ou rede do host. Os horários, SLAs e impactos dos incidentes são exemplos didáticos.

## Competências demonstradas

Administração Linux • Diagnóstico de problemas • Bash • Permissões • Logs • Serviços • Redes • Backup e restauração • Documentação de incidentes • Docker • CI/CD.

[Voltar ao perfil](../../README.md)
