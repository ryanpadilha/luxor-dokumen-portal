# -*- coding: utf-8 -*-
# Application Factory

from os import path
from flask import Flask
from .blueprints.events import events_blueprint
from .blueprints.garages import garages_blueprint
from .blueprints.events_api import EventAPI

from flask_restful import Api
from .db import db, dbsql
from .cache import cache


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )

    app = Flask('wtf',
                instance_path=instance_path,
                instance_relative_config=True)

    # read constants of the current file
    # app.config.from_object(__name__)

    # read constants from module, absolute path
    app.config.from_object('wtf.default_settings')

    # read constants from system-environment
    # app.config.from_envvar(config_env_var, silent=False)

    # read constants from python-file
    app.config.from_pyfile('config.cfg')

    # read constants from json-file
    # app.cofig.update(**extra_config)

    app.register_blueprint(events_blueprint)
    app.register_blueprint(garages_blueprint, url_prefix='/intern')  # diff url mount

    api_v1 = Api(app)
    api_v1.add_resource(EventAPI, '/api/v1/events')

    db.init_app(app)
    cache.init_app(app)
    dbsql.init_app(app)

    with app.test_request_context():
        dbsql.create_all()

    return app
