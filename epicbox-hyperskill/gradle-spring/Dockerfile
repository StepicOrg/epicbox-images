FROM gradle:6.5.1-jdk11

USER root
RUN apt-get update && \
    apt-get install --yes python3 && \
    rm -rf /var/lib/apt/lists/*
USER gradle

COPY --chown=gradle checker/ /checker/

RUN gradle --info --no-daemon --project-dir=/checker/sandbox test && \
    cp -r /home/gradle/.gradle /home/gradle/.gradle_cache && \
    rm -rf /checker/sandbox/files/*
