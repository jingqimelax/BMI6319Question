FROM python:3

WORKDIR /app/

COPY bin /app/bin
RUN cd /app/bin/liblinear-2.30/ && make clean && make

COPY src /app/src
COPY run.sh /app/run.sh
