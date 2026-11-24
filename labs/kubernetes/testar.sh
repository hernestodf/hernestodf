#!/usr/bin/env bash
set -euo pipefail
[[ "$(kubectl config current-context)" == "kind-profox-lab" ]]
ns=profox-k8s-demo
if kubectl get namespace "$ns" >/dev/null 2>&1; then
  echo "Namespace ja existe; use cluster descartavel"; exit 1
fi
kubectl apply -f app.yaml
trap 'kubectl delete namespace "$ns" --wait=false' EXIT
kubectl -n "$ns" rollout status deployment/portal --timeout=180s
kubectl -n "$ns" run cliente --image=busybox:1.37 --restart=Never --command -- sleep 300
kubectl -n "$ns" wait --for=condition=Ready pod/cliente --timeout=120s
kubectl -n "$ns" exec cliente -- wget -qO- http://portal/ | grep -qi 'welcome to nginx'
pod=$(kubectl -n "$ns" get pods -l app=portal -o jsonpath='{.items[0].metadata.name}')
kubectl -n "$ns" delete pod "$pod" --wait=true
kubectl -n "$ns" rollout status deployment/portal --timeout=180s
[[ "$(kubectl -n "$ns" get deployment portal -o jsonpath='{.status.readyReplicas}')" == "2" ]]
kubectl -n "$ns" exec cliente -- wget -qO- http://portal/ | grep -qi 'welcome to nginx'
