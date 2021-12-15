FROM gradle:7.3-jdk11

COPY --chown=gradle checker/ /checker/

RUN gradle --no-daemon --project-dir=/checker/template test && \
    rm -rf /checker/template/src/* && \
    rm -rf /checker/template/test/*
