FROM trikset/checker-stepik:2019.6
MAINTAINER Iakov Kirilenko <Iakov.Kirilenko@trikset.com>
ENV LANG ru_RU.UTF-8
RUN du -csh /* 2>/dev/null | sort -h || : ; grep sandbox /etc/passwd
