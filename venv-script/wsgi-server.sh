#!/bin/bash

exec gunicorn -w 6 --bind=0.0.0.0:8000 --user=ubuntu --log-level=debug --log-file=/var/wplex/logs/labix.orionxf.com.br/gunicorn.log 2>>/var/wplex/logs/labix.orionxf.com.br/gunicorn.log wsgi:application &