# Wazuh SIEM — Triagem de eventos de segurança
Exemplo de regra local Wazuh para falhas repetidas de autenticação SSH, logs fictícios e simulador Python de correlação temporal. O simulador não reproduz integralmente o motor de regras Wazuh.
```sh
python3 -m unittest -v
python3 correlacionar.py
```
Em instalação Wazuh autorizada, confira a regra 5716 na versão instalada, use ID local não utilizado, copie a regra para o arquivo local de regras e valide com wazuh-logtest antes de reiniciar o manager. O CI valida XML e simulador, não executa Wazuh nem comprova que a regra dispara no motor real.
Runbook: confirmar origem, usuário e janela temporal; distinguir falha legítima de ataque; preservar logs; escalar conforme impacto. Não bloqueie IPs automaticamente.