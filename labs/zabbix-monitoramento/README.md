# Laboratório Zabbix — Monitoramento e Operações de TI

Ambiente didático independente com Zabbix 7.0 LTS, PostgreSQL, interface web e agente Linux em Docker Compose. Nenhum dado empresarial é utilizado.

## Instalação local

```bash
cd labs/zabbix-monitoramento
cp .env.example .env
# Edite .env e escolha uma senha exclusiva.
docker compose up -d
docker compose logs -f server
```

Acesse http://127.0.0.1:8088 após a inicialização do banco. O login inicial padrão do Zabbix é Admin / zabbix; altere imediatamente a senha. Não exponha a interface à Internet. As imagens usam a série 7.0 com tags móveis; fixe versões/digests antes de qualquer implantação real.

## Exercício

Em Coleta de dados → Hosts, cadastre o host fictício `laboratorio-demo`, interface agente com DNS `agent`, porta 10050, conexão por DNS. Vincule o template Linux by Zabbix agent. Aguarde a coleta e confira os dados recentes.

Consulte [roteiro de monitoramento](docs/monitoramento.md) e [incidente simulado](docs/incidente.md).

## Validação

```bash
python3 -m unittest discover -s tests -v
docker compose config -q
```

O CI valida o Compose e o simulador de estados de alerta; não comprova a inicialização completa do Zabbix, importação de templates ou disparo real de triggers. Os exemplos de expressão precisam ser configurados e conferidos na interface.

Para encerrar sem apagar o banco: `docker compose down`.

**Não é uma configuração pronta para produção:** requer TLS, gestão de segredos, backups, controle de acesso, dimensionamento e validação operacional.
