FROM golang:1.23-alpine AS builder
WORKDIR /src
COPY go.mod ./
COPY cmd/ ./cmd/
RUN CGO_ENABLED=0 GOOS=linux go build -trimpath -ldflags="-s -w" -o /server ./cmd/server
FROM alpine:3.21
RUN addgroup -S app && adduser -S -G app app
USER app
COPY --from=builder /server /server
EXPOSE 8080
ENTRYPOINT ["/server"]
