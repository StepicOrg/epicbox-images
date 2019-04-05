FROM gradle:5.3.1-jdk11-slim

COPY --chown=gradle checker/ /checker/

USER root
RUN apt-get update && \
    apt-get install --yes python3
USER gradle

RUN gradle --project-dir=/checker/template test && \
    cp -r /home/gradle/.gradle /home/gradle/.gradle_cache && \
    rm -rf /checker/template/project/task/src/* && \
    rm -rf /checker/template/project/task/test/*
