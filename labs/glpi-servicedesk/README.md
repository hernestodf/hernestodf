# GLPI e ITIL — Service Desk e inventário
Modelo offline de chamados e SLA com inventário fictício, mais roteiro prático para GLPI. Não substitui o GLPI e não usa sua API.
```sh
python3 -m unittest -v
python3 sla.py
```
Em uma instalação isolada do GLPI, crie entidade Laboratório, perfis solicitante/técnico, categorias Rede, Sistemas, Acesso, ativos fictícios e regras de SLA. Abra chamados, associe ativos, atribua técnico, registre atendimento e solução, teste escalonamento. Use calendário e pausas conforme a política de atendimento. O script usa horas corridas UTC e não modela calendário ou suspensão de SLA.
SLA é compromisso de serviço, incidente é interrupção/degradação, requisição é pedido padrão. Prioridade deve considerar impacto e urgência. A regra de SLA do exemplo não representa política empresarial.