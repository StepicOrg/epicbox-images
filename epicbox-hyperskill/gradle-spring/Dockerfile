FROM gradle:8.5-jdk17

COPY --chown=gradle checker/ /checker/

ENV GRADLE_USER_HOME=/home/gradle/gradle_cache

RUN gradle --info --no-daemon --project-dir=/checker/sandbox test && \
    rm -rf /checker/sandbox/files/*
