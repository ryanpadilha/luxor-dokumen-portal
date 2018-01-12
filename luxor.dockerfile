#
# Dockerfile -- Container Image for Debian 9.3 / Oracle JRE Server 8
#
# build : docker build -f luxor.dockerfile -t python-luxor .
# tag   : docker tag python-luxor wplex/python-luxor:latest
# push  : docker push wplex/python-luxor
#

FROM python:3.6-jessie
LABEL maintainer="Ryan Padilha <ryan.padilha@wplex.com.br>"

ENV APP_DIR /var/wplex/www/labix.orionxf.com.br
ENV LOG_FILE /var/wplex/logs/labix.orionxf.com.br/gunicorn.log

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY . .

RUN pip install --upgrade pip \
 && pip install -r venv-script/requirements.txt

EXPOSE 8000
ENTRYPOINT exec gunicorn -w 6 --bind=0.0.0.0:8000 --log-level=debug --log-file=$LOG_FILE 2>>$LOG_FILE wsgi:application &

# HEALTHCHECK CMD curl --fail http://localhost:$APP_PORT || exit 1