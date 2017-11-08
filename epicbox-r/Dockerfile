FROM r-base:3.4.2
MAINTAINER Pavel Sviderski <ps@stepik.org>

RUN useradd -M -d /sandbox sandbox

RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl-dev libcurl4-openssl-dev \
 && rm -rf /var/lib/apt/lists/*

RUN Rscript -e 'install.packages(c("Rcpp","ggplot2","psych","dplyr","stringr","tidyr","data.table","plotly","lme4","lmerTest","mlmRev","sjPlot"))'
