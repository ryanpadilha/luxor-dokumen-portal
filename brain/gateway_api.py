# -*- coding: utf-8 -*-
# Application Factory

from os import path
from flask import Flask
from .blueprints.events import events_blueprint
from flask_restful import Api


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )

    app = Flask('brain',
                instance_path=instance_path,
                instance_relative_config=True)

    # read constants of the current file
    # app.config.from_object(__name__)

    # read constants from module, absolute path
    app.config.from_object('brain.default_settings')

    # read constants from system-environment
    # app.config.from_envvar(config_env_var, silent=False)

    # read constants from python-file
    app.config.from_pyfile('config.cfg')

    # read constants from json-file
    # app.cofig.update(**extra_config)

    app.register_blueprint(events_blueprint)

    return app
