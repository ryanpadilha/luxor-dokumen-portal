# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, jsonify, current_app

events_blueprint = Blueprint('events', __name__)


@events_blueprint.route('/')
@events_blueprint.route('/home')
def home():
    return render_template('pages/home.html'), 200
