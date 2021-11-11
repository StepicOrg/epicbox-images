FROM gradle:7.2-jdk17

COPY --chown=gradle checker/ /checker/

RUN gradle --info --no-daemon --project-dir=/checker/sandbox test && \
    rm -rf /checker/sandbox/files/*
