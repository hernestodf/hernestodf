FROM debian:bookworm-slim
WORKDIR /laboratorio
COPY scripts/backup-demo.sh /laboratorio/backup-demo.sh
USER 65534:65534
ENTRYPOINT ["bash", "/laboratorio/backup-demo.sh"]
