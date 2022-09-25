# -*- coding: utf-8 -*-
"""This module creates the routes for our API."""

import random

from flask import request

from API import app


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def api_home() -> dict:
    """Handle get requests to /api/v1 route.

    Returns
    -------
    dict:
        A dictionary showing:
        {
            'data': 'Hello from shileds.io json endpoint'
        }
    """
    data = {
        'data': 'Hello from shileds.io json endpoint'
    }

    return data, 200


@app.route('/api/v1/data', methods=['GET'])
def shields_io_data() -> dict:
    """Generate JSON data for the shields.io server.

    Parameters
    ----------
    username: str
        The users name

    Returns
    -------
    data: dict
        This dictionary contains info used to generate the dynamic badge by shields.io
            data = {
            "schemaVersion": 1,
            "label": "name",
            "message": "username",
            "color": "color-name",
            "labelColor": "color-name",
            "style": "style-name"
            }
    """
    if request.args.get('username'):
        username = request.args.get('username')
        colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple', 'grey']
        styles = ['flat', 'plastic', 'flat-square', 'for-the-badge', 'social']
        data = {
            "schemaVersion": 1,
            "label": "name",
            "message": username,
            "color": random.choice(colors),
            "labelColor": random.choice(colors),
            "style": random.choice(styles)
        }

        return data, 200

    error = {
        'error': 'You must include your name in the request.'
    }
    return error, 400
