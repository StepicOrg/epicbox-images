FROM gradle:8.5.0-jdk17

COPY --chown=gradle checker/ /checker/

ENV GRADLE_USER_HOME=/home/gradle/gradle_cache

RUN gradle --no-daemon --project-dir=/checker/template test && \
    rm -rf /checker/template/src/* && \
    rm -rf /checker/template/test/*
