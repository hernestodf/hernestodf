#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

workdir="$(mktemp -d)"
trap 'rm -rf -- "$workdir"' EXIT
mkdir -p "$workdir/origem/config" "$workdir/origem/logs" "$workdir/restaurado"
printf '%s\n' 'ambiente=exemplo' 'servico=demo' > "$workdir/origem/config/aplicacao.conf"
printf '%s\n' '2026-01-01T10:00:00Z INFO serviço de demonstração iniciado' > "$workdir/origem/logs/aplicacao.log"

tar -czf "$workdir/backup.tar.gz" -C "$workdir/origem" .
tar -tzf "$workdir/backup.tar.gz" >/dev/null
tar -xzf "$workdir/backup.tar.gz" -C "$workdir/restaurado"

diff -r "$workdir/origem" "$workdir/restaurado"
printf '%s\n' 'Backup e restauração fictícios validados com sucesso.'
