# DevSecOps — Trivy e Gitleaks
Pipeline de segurança com scanners reais em containers: Gitleaks inspeciona a pasta atual e Trivy verifica configuração do Dockerfile. O teste negativo usa fixture sintética de container executado como root, fora da pasta auditada, e exige detecção pelo scanner.
```sh
bash testar.sh
```
Não há tokens reais nem publicação de imagens. O exame não cobre histórico Git, código em execução, todos os tipos de vulnerabilidade ou dependências. Produção exige varredura de imagens/dependências, atualização de bases, gestão de exceções, rotação de segredos e revisão de resultados. Não trate um CI verde como certificação de segurança.