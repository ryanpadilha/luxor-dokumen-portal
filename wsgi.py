# -*- coding: utf-8 -*-

# entry point for the application based on WSGI

from brain.gateway_api import create_app

application = create_app(mode='null')

if __name__ == '__main__':
    application.run()
