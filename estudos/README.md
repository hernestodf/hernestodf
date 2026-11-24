# Minha jornada de aprendizado em TI — Hernesto Filho

Material pessoal de estudo e prática técnica de Hernesto Filho. Os laboratórios são iniciativas independentes de aprendizado, sem vínculo institucional com meus empregadores. Inspirado em aprendizagem visual, analogias e recuperação ativa do conhecimento.

![Mapa mental de Operações de TI](mapa-mental.svg)

[Ver SVG em tamanho integral](mapa-mental.svg)

## Como estudar

Leia a analogia, explique o conceito sem consultar o texto, execute o laboratório em ambiente isolado e responda à pergunta. Registre evidências e erros encontrados. Os projetos são demonstrações, não comprovação de implantação em produção.

## 1. Redes e MikroTik

**Entenda:** Pense em uma cidade: IP é o endereço, DNS é a agenda e o gateway é a saída para outras redes. DHCP fornece endereços e outros parâmetros; VLAN separa domínios de broadcast; firewall controla tráfego. Um switch encaminha quadros e um roteador encaminha pacotes entre redes.

**Pratique:** `ip addr`, `ip route`, `ping`, `dig`, `ss -tuln`. Se o IP funciona e o nome não, investigue resolução DNS antes de mudar a rede.

**Pergunta de entrevista:** Explique por que VLAN não equivale a VPN.

[Laboratório correspondente](../labs/redes-mikrotik/README.md)

## 2. Administração Linux

**Entenda:** O kernel administra recursos; processos executam tarefas e serviços podem ser gerenciados pelo systemd. Logs ajudam a correlacionar sintomas com eventos. Memória livre baixa não prova falta de RAM: observe memória disponível, swap e pressão de memória.

**Pratique:** `top`, `free -h`, `df -h`, `df -i`, `systemctl status`, `journalctl -u SERVICO`. Em lentidão, avalie CPU, memória, disco, rede e logs; não reinicie sem investigar.

**Pergunta de entrevista:** Qual a diferença entre df e du?

[Laboratório correspondente](../labs/linux-administracao/README.md)

## 3. NOC, Zabbix e observabilidade

**Entenda:** O NOC é uma central de sinais vitais. No Zabbix, host representa um recurso, item coleta dados, trigger avalia condições e template reutiliza configurações. Prometheus coleta métricas; Grafana visualiza; Alertmanager agrupa e encaminha notificações. SLA é o acordo de nível de serviço; MTTA mede reconhecimento e MTTR depende da definição operacional adotada.

**Pratique:** Execute o simulador NOC e compare estados saudável, falha e recuperação. No Zabbix, configure o agente no ambiente de teste e valide coleta e triggers. Registre impacto, evidências, escalonamento e recuperação.

**Pergunta de entrevista:** Qual a diferença entre métrica, alerta e incidente?

[Laboratório correspondente](../labs/noc-monitoring-lab/README.md) · [Laboratório Zabbix](../labs/zabbix-monitoramento/README.md)

## 4. Active Directory e PowerShell

**Entenda:** AD DS centraliza identidades e computadores em domínios; o controlador de domínio presta serviços de diretório e autenticação. OUs organizam objetos e permitem delegação e vinculação de GPOs; grupos atribuem acessos. Kerberos autentica e LDAP permite consultar o diretório. DNS correto é essencial.

**Pratique:** Em ambiente autorizado: `Get-ADUser -Filter *`, `Get-ADGroup -Filter *`, `gpresult /r`, `Resolve-DnsName`. Investigue domínio, DNS, horário, conta e políticas quando um login falha.

**Pergunta de entrevista:** Qual a diferença entre uma OU e um grupo de segurança?

[Laboratório correspondente](../labs/active-directory/README.md)

## 5. Hardening e segurança

**Entenda:** Segurança em camadas reduz superfície de ataque: atualizações, firewall, autenticação, permissões, auditoria e backup. Permissão 600 significa leitura e escrita pelo proprietário, sem permissões para grupo ou outros. MFA exige fatores distintos e RBAC distribui acesso por funções.

**Pratique:** Revise `ss -tuln`, `ls -l` e, com autorização, `sshd -T`. Teste mudanças em VM com acesso alternativo, evitando bloquear o próprio SSH. O auditor do lab analisa apenas dados didáticos.

**Pergunta de entrevista:** Por que desativar autenticação por senha exige validar uma alternativa primeiro?

[Laboratório correspondente](../labs/hardening-linux/README.md)

## 6. Proxmox VE

**Entenda:** Imagine um prédio: VMs são apartamentos com sistemas operacionais próprios; LXC compartilha o kernel Linux do host. KVM fornece virtualização, bridges conectam redes e storage guarda discos. Snapshot preserva um estado, mas não substitui backup independente.

**Pratique:** Em host de teste autorizado: `pveversion`, `qm list`, `pct list`, `pvesm status`. Planeje memória, CPU e disco; restaure backup com ID distinto e valide a aplicação.

**Pergunta de entrevista:** Quando escolher VM em vez de LXC?

[Laboratório correspondente](../labs/proxmox/README.md)

## 7. Microsoft 365, Entra ID, Azure e AWS

**Entenda:** Microsoft 365 oferece serviços SaaS, como Exchange Online, Teams e SharePoint. Entra ID gerencia identidades em nuvem e não é equivalente ao AD DS. Azure VM e EC2 oferecem IaaS; VNet e VPC são redes virtuais; Blob e S3 armazenam objetos. Azure RBAC e AWS IAM controlam acesso com modelos distintos.

**Pratique:** Execute os auditores Python e PowerShell do inventário fictício. Investigue login por licença, identidade, MFA, políticas e estado do serviço. Qualquer conta real exige autorização e controle de custos.

**Pergunta de entrevista:** Compare IaaS, PaaS e SaaS. Qual a função de MFA e do menor privilégio?

[Laboratório correspondente](../labs/cloud-m365-azure-aws/README.md)

## 8. Docker e DevOps

**Entenda:** Dockerfile é a receita; imagem é o pacote; container é a instância em execução. Volumes persistem dados e redes conectam serviços. Compose descreve múltiplos containers. CI automatiza integração e validação; CD entrega ou implanta alterações conforme o fluxo adotado.

**Pratique:** `docker compose config`, `docker compose up -d`, `docker compose ps`, `docker compose logs`. Verifique testes, build e health checks antes de deploy. Revise o GitHub Actions do laboratório.

**Pergunta de entrevista:** Por que um container não substitui um backup de banco?

[Laboratório correspondente](../labs/profox-devops-lab/README.md)

## 9. Backend Go e PostgreSQL

**Entenda:** Uma requisição HTTP chega ao handler Go, passa pelas regras de negócio e usa pgx para consultar PostgreSQL. CRUD organiza operações sobre dados. Migrations versionam o esquema; transações agrupam operações atômicas; consultas parametrizadas evitam injeção SQL. Health e readiness têm objetivos distintos.

**Pratique:** `go test ./...`, `go vet ./...`, `curl` nos endpoints documentados. Rode o Compose de teste e confira persistência, respostas HTTP e erros.

**Pergunta de entrevista:** Qual a diferença entre health check e readiness?

[Laboratório correspondente](../labs/profox-go-backend/README.md)

## 10. Automação de Jobs e Steps

**Entenda:** Imagine uma linha de montagem: a validação depende da extração, e a consolidação depende da validação. Um DAG (grafo direcionado acíclico) organiza essas dependências. Retry tenta novamente uma operação; reprocessamento exige cuidado com duplicação. Idempotência significa que repetir uma operação produz o mesmo efeito pretendido.

**Pratique:** Execute python3 jobs.py e python3 -m unittest -v. Provoque falha transitória, falha definitiva e ciclo de dependências. Observe o bloqueio dos steps dependentes e a continuidade dos independentes.

**Pergunta de entrevista:** Por que não se deve reprocessar um job financeiro automaticamente sem verificar idempotência e estado?

[Laboratório correspondente](../labs/jobs-steps/README.md)

## 11. SQL Troubleshooting

**Entenda:** Um índice funciona como o índice de um livro: reduz o trabalho para localizar dados, mas tem custo de manutenção. EXPLAIN estima um plano; EXPLAIN ANALYZE executa a consulta. Transações preservam atomicidade. Lock é uma proteção de concorrência; deadlock é um ciclo de espera, diferente de simples contenção.

**Pratique:** Inicie o PostgreSQL descartável conforme o README. Compare planos com e sem índice, valide rollback e execute bash test_lock.sh para observar timeout entre sessões.

**Pergunta de entrevista:** Como identificar a sessão bloqueadora? Por que um índice nem sempre é usado?

[Laboratório correspondente](../labs/sql-troubleshooting/README.md)

## 12. Terraform e Ansible

**Entenda:** Terraform é a planta da infraestrutura: descreve recursos e acompanha seu estado. Ansible é a equipe que configura o ambiente. Plan mostra mudanças previstas; apply aplica; state registra vínculos com recursos. Idempotência evita alterações desnecessárias em execuções repetidas.

**Pratique:** Execute bash testar.sh. Observe o recurso local terraform_data, a saída JSON e o playbook. A segunda execução verifica ausência de mudanças no Ansible e o plan confirma estabilidade.

**Pergunta de entrevista:** Qual a diferença entre provisionamento e configuração? Por que proteger o state?

[Laboratório correspondente](../labs/terraform-ansible/README.md)

## 13. Backup e Disaster Recovery

**Entenda:** Backup é uma cópia; recuperação é a capacidade de voltar a operar. RPO define a perda tolerável em tempo, RTO o prazo alvo de recuperação. Hash verifica integridade contra um valor esperado confiável; não substitui assinatura nem cópia independente.

**Pratique:** Execute python3 recuperar.py e python3 -m unittest -v. Verifique restauração em outro diretório, recusa de hash incorreto e caminho inseguro. Cronometre uma restauração e compare com um RTO didático.

**Pergunta de entrevista:** Se o RPO é 1 hora e o último backup tem 4 horas, o objetivo foi atendido?

[Laboratório correspondente](../labs/disaster-recovery/README.md)

## 14. Kubernetes

**Entenda:** Deployment mantém o número desejado de réplicas; Pods executam containers; Service oferece endereço estável. Readiness indica prontidão para tráfego e liveness detecta necessidade de reinício. O controlador substitui Pods perdidos; isso não garante alta disponibilidade física.

**Pratique:** Crie o cluster kind descartável conforme README. Execute bash testar.sh, observe rollout, teste HTTP e substituição de um Pod. Use kubectl describe, logs e get events no namespace de teste.

**Pergunta de entrevista:** Qual a diferença entre Deployment e Service? Por que readiness não é igual a liveness?

[Laboratório correspondente](../labs/kubernetes/README.md)

## 15. SIEM e Wazuh

**Entenda:** Um SIEM é como uma central de segurança: correlaciona eventos para ajudar na triagem. Cinco falhas SSH em uma janela de 60 segundos podem sugerir atividade suspeita, mas não provam ataque. Uma regra relaciona eventos, origem e intervalo.

**Pratique:** Execute os testes do correlacionador; altere a janela e a origem dos eventos. No Wazuh real, valide decodificação e regra com wazuh-logtest em ambiente autorizado.

**Pergunta de entrevista:** Qual a diferença entre alerta, falso positivo e incidente?

[Laboratório correspondente](../labs/wazuh-siem/README.md)

## 16. DevSecOps

**Entenda:** Segurança precisa integrar o fluxo de entrega. Gitleaks identifica padrões de segredos e Trivy avalia configurações e outros riscos conforme os scanners escolhidos. Um resultado limpo não prova ausência de vulnerabilidade.

**Pratique:** Execute bash testar.sh e compare a configuração aceita com a fixture root detectada. Nunca publique segredos para testar um scanner.

**Pergunta de entrevista:** Qual a diferença entre escanear configuração, dependências e segredos?

[Laboratório correspondente](../labs/devsecops/README.md)

## 17. Keycloak e identidade

**Entenda:** OAuth 2.0 delega autorização; OpenID Connect adiciona identidade. Um realm delimita configuração de identidade, cliente é uma aplicação, token representa autorização conforme o fluxo. SSO permite reutilizar uma sessão de autenticação entre aplicações.

**Pratique:** Execute o Compose e testar.py. Compare descoberta OIDC, obtenção de token de serviço e rejeição de segredo inválido. Para login humano, pratique Authorization Code com PKCE separadamente.

**Pergunta de entrevista:** Qual a diferença entre autenticação e autorização? Quando usar client credentials?

[Laboratório correspondente](../labs/keycloak-iam/README.md)

## 18. GLPI e ITIL

**Entenda:** Uma central de serviços organiza chamados e ativos. Impacto e urgência ajudam a definir prioridade. SLA expressa compromisso de serviço, enquanto inventário relaciona equipamentos e responsáveis. Um incidente não é necessariamente uma requisição.

**Pratique:** Execute sla.py e os testes de prazo. No GLPI autorizado, configure perfis, entidades, ativos e chamados fictícios; compare o SLA com o calendário configurado.

**Pergunta de entrevista:** Como diferenciar incidente, requisição e problema?

[Laboratório correspondente](../labs/glpi-servicedesk/README.md)

## 19. Nginx e HAProxy

**Entenda:** Um proxy reverso recebe requisições em nome de servidores internos. O balanceador distribui carga entre backends; health checks ajudam a retirar instâncias indisponíveis. Isso não elimina um ponto único de falha no próprio balanceador.

**Pratique:** Execute o Compose e testar.sh. Observe as respostas dos dois backends e pare um deles para verificar continuidade.

**Pergunta de entrevista:** Qual a diferença entre proxy reverso e balanceamento de carga?

[Laboratório correspondente](../labs/proxy-balanceamento/README.md)

## 20. RabbitMQ e Redis

**Entenda:** Fila desacopla produtor e consumidor. Confirmação de processamento e idempotência ajudam a lidar com falhas e entregas repetidas. Cache reduz latência e carga; TTL limita a vida útil de uma entrada.

**Pratique:** Execute testar.py para publicar e consumir mensagem fictícia pela API de gerenciamento e verificar expiração de cache Redis.

**Pergunta de entrevista:** Por que uma fila não garante exatamente uma vez? Quando invalidar cache?

[Laboratório correspondente](../labs/mensageria-cache/README.md)

## 21. Jenkins e GitLab CI

**Entenda:** Pipeline descreve etapas reproduzíveis. Agentes ou runners executam tarefas; artefatos registram resultados de build. Configurações declarativas variam por plataforma, mas scripts portáveis reduzem duplicação.

**Pratique:** Execute pipeline.sh; revise Jenkinsfile e .gitlab-ci.yml. Em instâncias de teste, rode o mesmo pipeline e confira o artefato.

**Pergunta de entrevista:** Qual a diferença entre runner, job, stage e artefato?

[Laboratório correspondente](../labs/jenkins-gitlab-ci/README.md)

## 22. Loki e OpenTelemetry

**Entenda:** OpenTelemetry padroniza coleta e exportação de telemetria. Collector recebe, processa e encaminha sinais. Loki armazena logs consultados por LogQL. Logs, métricas e traces são sinais complementares; este lab cobre logs OTLP.

**Pratique:** Execute o Compose e testar.py; acompanhe um evento fictício da entrada OTLP até a consulta no Loki. Experimente filtros com rótulos de baixa cardinalidade.

**Pergunta de entrevista:** Qual a diferença entre log, métrica e trace?

[Laboratório correspondente](../labs/observabilidade-avancada/README.md)

## Revisão de 60 dias

| Período | Tema |
|---|---|
| Dias 1–4 | Redes |
| Dias 5–8 | Linux |
| Dias 9–12 | NOC e Zabbix |
| Dias 13–16 | AD e PowerShell |
| Dias 17–19 | Hardening |
| Dias 20–22 | Proxmox |
| Dias 23–26 | Microsoft 365 e Cloud |
| Dias 27–29 | Docker, Go e PostgreSQL |
| Dias 30–32 | Jobs e Steps |
| Dias 33–35 | SQL Troubleshooting |
| Dias 36–38 | Terraform e Ansible |
| Dias 39–41 | Disaster Recovery |
| Dias 42–44 | Kubernetes |
| Dias 45–46 | SIEM e Wazuh |
| Dias 47–48 | DevSecOps |
| Dias 49–50 | Keycloak |
| Dias 51–52 | GLPI e ITIL |
| Dias 53–54 | Nginx e HAProxy |
| Dias 55–56 | RabbitMQ e Redis |
| Dia 57 | Jenkins e GitLab CI |
| Dias 58–59 | Loki e OpenTelemetry |
| Dia 60 | Revisão integrada e entrevista |
