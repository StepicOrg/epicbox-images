FROM gradle:7.2.0-jdk11

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
