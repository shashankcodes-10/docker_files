FROM dhi.io/golang:1.26-alpine-dev AS builder

WORKDIR /app

COPY . .

RUN go mod tidy && \
    go mod download && \
    CGO_ENABLED=0 go build -o backend .

FROM dhi.io/golang:1.26-alpine-dev

WORKDIR /app

COPY --from=builder /app/backend /app/backend

EXPOSE 8000

CMD ["./backend"]
