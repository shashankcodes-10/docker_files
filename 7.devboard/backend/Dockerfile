#------------------------builder-------------------
FROM dhi.io/golang:1-alpine AS builder

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download 

COPY . .

RUN CGO_ENABLED=0 go build -o backend

#-----------------------runner-----------------------
FROM  dhi.io/golang:1-alpine

WORKDIR /app

COPY --from=builder /app/backend /app/backend

EXPOSE 8080

ENTRYPOINT ["./backend"]

