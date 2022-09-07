FROM python:3.10-slim

RUN apt-get update && \
    apt-get install --yes bc && \
    apt-get install --yes git && \
    apt-get install --yes sqlite3 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache \
  https://github.com/hyperskill/hs-test-python/archive/v9.tar.gz \
  GitPython==3.1.27

COPY checker/ /checker/
