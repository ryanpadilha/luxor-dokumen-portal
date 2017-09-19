# -*- coding: utf-8 -*-

import sys
from brain.gateway_api import create_app

mode = sys.argv[1] if len(sys.argv) > 1 else 'development'
application = create_app(mode=mode)
application.run(**application.config.get_namespace('RUN_'))
