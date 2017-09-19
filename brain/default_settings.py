# -*- coding: utf-8 -*-

import os

DEBUG = False
USE_RELOADER = False
HOST = '0.0.0.0'
RUN_PORT = int(os.environ.get('PORT', 5000))

WTF_CSRF_ENABLED = True
SECRET_KEY = '2ea86827d6c7226af5bad77671a5c08d'  # sk-luXOR-p0r7@1-F1N

basedir = os.path.abspath(os.path.dirname(__file__))
