"""
Empty module docstring
"""
from crypt import methods
from API import app
import random


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def api_home() -> str:
    """Handles get requests to /api/v1 route

    Returns
    -------
    str:
        A string showing the welcome message : 'Hello from flask e-commerce api!'
    """

    return "Hello from flask e-commerce api!", 200


@app.route('/api/v1/data/<id>', methods=['GET'])
def shields_io_data(id):
    colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple', 'grey']
    styles = ['flat', 'plastic', 'flat-square', 'for-the-badge', 'social']
    data = {
        "schemaVersion": 1,
        "label": "name",
        "message": "lyle okoth",
        "color": random.choice(colors),
        "labelColor": random.choice(colors),
        "style": random.choice(styles)
        }

    return data, 200