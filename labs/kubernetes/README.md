# Kubernetes — Deploy, Service e recuperação

Use um cluster descartável kind. O manifesto declara duas réplicas Nginx com limites de recursos, probes HTTP e Service ClusterIP. Não exponha o serviço publicamente. O CI cria cluster local, verifica rollout, resposta HTTP e substituição de um Pod após exclusão. Não configura HA de nós, armazenamento persistente, TLS nem segurança de produção.

## Exercício
Com Docker, kind e kubectl instalados:
```sh
kind create cluster --name profox-lab
kubectl config use-context kind-profox-lab
bash testar.sh
kind delete cluster --name profox-lab
```
O script exige contexto kind-profox-lab e namespace exclusivo. Não execute em cluster de produção.

## Troubleshooting
Deployment mantém réplicas desejadas; Pod contém containers; Service oferece acesso estável. Readiness decide se o Pod recebe tráfego; liveness detecta necessidade de reiniciar o container. Use kubectl get pods, describe, logs e get events no namespace do lab. Confira imagem, recursos, probes e endpoints antes de mudar configurações.
