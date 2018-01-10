#
# Dockerfile -- Container Image for Debian 9.3 / Oracle JRE Server 8
#
# build : docker build -f debian-oracle-server-jre8.dockerfile -t debian-server-jre8 .
# tag   : docker tag debian-server-jre8 wplex/debian-server-jre8:latest
# push  : docker push wplex/debian-server-jre8
#

FROM python:3.6-jessie
LABEL maintainer="Ryan Padilha <ryan.padilha@wplex.com.br>"

RUN mkdir -p /var/wplex/www/labix.orionxf.com.br
COPY venv-script/requirements.txt /var/wplex/www/labix.orionxf.com.br



