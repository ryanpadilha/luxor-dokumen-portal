# -*- coding: utf-8 -*-

# entry point for the application based on WSGI

import sys
from brain.gateway_api import create_app

mode = 'production'
application = create_app(mode=mode)
application.run(**application.config.get_namespace('RUN_'))
