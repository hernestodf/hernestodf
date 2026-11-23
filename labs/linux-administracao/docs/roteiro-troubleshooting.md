# Roteiro de diagnóstico Linux — somente leitura

> Execute comandos apenas em sistemas sob sua administração ou com autorização. Este roteiro não altera serviços ou configurações.

## 1. Identificar o sistema

```bash
uname -a
cat /etc/os-release
uptime
id
```

## 2. CPU e memória

```bash
free -h
uptime
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
```

Observe carga, memória disponível, swap e processos que consomem recursos. Carga elevada não significa necessariamente CPU saturada.

## 3. Disco e arquivos

```bash
df -h
df -i
du -sh /var/log 2>/dev/null
ls -lah /var/log | head
```

Compare espaço livre e inodes. **Não apague logs sem política de retenção e autorização.**

## 4. Serviços e logs

```bash
systemctl --failed
systemctl status ssh --no-pager
journalctl -p err -n 30 --no-pager
```

O nome do serviço SSH pode variar por distribuição; `systemctl` requer systemd. Em contêineres mínimos, esses comandos podem não estar disponíveis.

## 5. Rede e DNS

```bash
ip addr
ip route
getent hosts localhost
ss -tuln
```

Para investigar um domínio externo, confirme autorização e conectividade antes de realizar testes de rede. O laboratório automatizado não realiza conexões externas.

## 6. Registro de incidente

Documente início, sintoma, impacto, hipótese, comandos utilizados, evidências sanitizadas, ação e validação. Consulte [o exemplo de incidente](../incidentes/INC-LINUX-001.md).
