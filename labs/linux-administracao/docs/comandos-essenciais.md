# Comandos Linux essenciais para entrevistas de Suporte N2

| Pergunta | Comandos de leitura | O que analisar |
|---|---|---|
| Qual é a versão do Linux? | `cat /etc/os-release`, `uname -r` | Distribuição e kernel |
| O disco está cheio? | `df -h`, `df -i` | Espaço e inodes |
| O que consome memória? | `free -h`, `ps aux --sort=-%mem` | Disponibilidade e processos |
| O serviço falhou? | `systemctl status SERVICO` | Estado e mensagens |
| Quais erros ocorreram? | `journalctl -p err -n 30` | Eventos recentes |
| A rede tem rota? | `ip route`, `ip addr` | Interface e gateway |
| O DNS resolve? | `getent hosts localhost` | Resolução local |
| Quais portas estão abertas? | `ss -tuln` | Serviços em escuta |
| Quem sou eu? | `id`, `groups` | Identidade e grupos |
| Como verificar permissões? | `ls -l`, `stat ARQUIVO` | Proprietário, grupo e modo |
| Como conferir backup? | `tar -tzf ARQUIVO.tar.gz` | Integridade da estrutura |

**Dica:** explique sempre a hipótese, o comando, a interpretação da saída e o próximo passo seguro.
