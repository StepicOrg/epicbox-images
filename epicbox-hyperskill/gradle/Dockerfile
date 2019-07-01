FROM gradle:5.3.1-jdk11-slim

USER root
RUN apt-get update && \
    apt-get install --yes python3 && \
    rm -rf /var/lib/apt/lists/*
USER gradle

COPY --chown=gradle checker/ /checker/

RUN gradle --no-daemon --project-dir=/checker/template test && \
    cp -r /home/gradle/.gradle /home/gradle/.gradle_cache && \
    rm -rf /checker/template/src/* && \
    rm -rf /checker/template/test/*
