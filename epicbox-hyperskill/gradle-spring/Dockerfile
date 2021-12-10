FROM gradle:7.3-jdk17

COPY --chown=gradle checker/ /checker/

RUN gradle --info --no-daemon --project-dir=/checker/sandbox test && \
    cp -r /home/gradle/.gradle /home/gradle/.gradle_cache && \
    rm -rf /checker/sandbox/files/*
