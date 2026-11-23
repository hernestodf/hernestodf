FROM golang:1.23-alpine AS build
WORKDIR /src
COPY go.mod ./
RUN go mod download
COPY cmd/ ./cmd/
RUN go mod tidy && CGO_ENABLED=0 go build -trimpath -o /api ./cmd/api
FROM alpine:3.21
RUN addgroup -S app && adduser -S -G app app
USER app
COPY --from=build /api /api
EXPOSE 8080
ENTRYPOINT ["/api"]
