# Jenkins e GitLab CI — pipelines portáveis
Pipeline declarativo Jenkins e .gitlab-ci.yml com as mesmas etapas de teste e empacotamento. O CI GitHub executa o script compartilhado e verifica o artefato. Não executa servidores Jenkins/GitLab nem valida seus parsers.
```sh
bash pipeline.sh
```
Para praticar em ambientes autorizados, configure Jenkins com Pipeline e agente Linux com Python 3; crie job Pipeline from SCM apontando para este Jenkinsfile. Em GitLab, use um projeto de teste cujo diretório raiz contenha estes arquivos e runner Docker. Ajuste o checkout conforme o repositório. Não coloque segredos no código. Deploy exige aprovação, credenciais protegidas e rollback.