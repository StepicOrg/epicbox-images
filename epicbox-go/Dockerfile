FROM golang:1.18.2-stretch

ENV GO111MODULE=on

RUN useradd -M -d /sandbox sandbox

WORKDIR /sandbox

COPY go.mod go.sum main.go /sandbox/

# Pre-cache modules by compiling main.go
RUN go mod download && \
    go mod verify && \
    go mod tidy && \
    go run main.go &&  \
    rm main.go &&  \
    chmod ugo-w go.mod go.sum
