FROM python:3.6-alpine

RUN apk add --no-cache gcc g++ make bash git

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

COPY . /usr/src/app

RUN chmod 777 docker-entrypoint.sh
RUN chmod 777 docker-testentrypoint.sh

EXPOSE 4444
