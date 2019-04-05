FROM gradle:5.3.1-jdk11

COPY --chown=gradle checker/ /checker/
RUN gradle --project-dir=/checker/template test && \
    cp -r /home/gradle/.gradle /home/gradle/.gradle_cache && \
    rm -rf /checker/template/project/task/src/* && \
    rm -rf /checker/template/project/task/test/*
