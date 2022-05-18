FROM golang:1.18.0-stretch
MAINTAINER MAINTAINER Stepik Team <team@stepik.org>

RUN useradd -M -d /sandbox sandbox

USER sandbox

WORKDIR /sandbox

ENV GO111MODULE=on

COPY --chown=sandbox go.mod go.sum main.go ./
# Precaching modules by compile main.go
RUN go mod download && go mod verify && go mod tidy && go run main.go && rm main.go && chmod ugo-w go.mod go.sum
