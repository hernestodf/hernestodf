FROM alpine:3.22
RUN adduser -D -u 10001 demo
USER 10001
HEALTHCHECK CMD test -r /etc/alpine-release || exit 1
CMD ["cat", "/etc/alpine-release"]
