# Roteiro de monitoramento

O agente monitora seu próprio contêiner, não o host Docker. Não monte o socket Docker nem diretórios sensíveis.

| Item | Chave ilustrativa | Finalidade |
|---|---|---|
| Disponibilidade | agent.ping | Resposta do agente |
| CPU | system.cpu.util | Utilização |
| Memória | vm.memory.size[available] | Memória disponível |
| Disco | vfs.fs.size[/,pused] | Ocupação |

Crie um item de agente com chave agent.ping e intervalo de 30 segundos, caso ainda não exista no template. Exemplo de expressão de trigger: `nodata(/laboratorio-demo/agent.ping,3m)=1`. Confirme o nome técnico do host e a existência do item antes de salvar.

Para simular perda de comunicação no laboratório, execute `docker compose stop agent`, aguarde a janela configurada e examine Problemas. Recupere com `docker compose start agent`. Registre evidências reais somente após executar o exercício.

O simulador Python é independente do Zabbix e demonstra transições de estado, sem enviar alertas reais.
