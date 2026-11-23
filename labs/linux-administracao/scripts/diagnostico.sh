#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

printf '%s\n' '=== LABORATÓRIO LINUX: DIAGNÓSTICO SOMENTE LEITURA ==='
printf '\n[Identidade e kernel]\n'
id
uname -sr
printf '\n[Uso de disco]\n'
df -h .
printf '\n[Memória]\n'
if command -v free >/dev/null 2>&1; then free -h; else echo 'Comando free não disponível'; fi
printf '\n[Processos com maior consumo de CPU (amostra)]\n'
if command -v ps >/dev/null 2>&1; then ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6 || true; else echo 'Comando ps não disponível'; fi
printf '\n[DNS local]\n'
if command -v getent >/dev/null 2>&1; then getent hosts localhost || true; fi
printf '\nNenhuma configuração foi modificada.\n'
