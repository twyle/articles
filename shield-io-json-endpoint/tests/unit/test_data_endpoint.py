# -*- coding: utf-8 -*-
"""This module tests the JSON endpoint."""
import json


def test_json_endpoint(client):
    """Tests that the home route returns ok message on GET request.

    GIVEN we have the /api/v1/data?username=lyle route
    WHEN we send a GET request
    THEN we should get a 200 OK response
    """
    username = 'lyle'
    resp = client.get(f'/api/v1/data?username={username}')
    assert resp.status_code == 200


def test_shields_io_data(client):
    """Tests that the home route returns ok message on GET request and the json data.

    GIVEN we have the /api/v1/data route
    WHEN we send a GET request
    THEN we should get a 200 OK response and a JSON data with the form:
    expected_data = {
        "schemaVersion": 1,
        "label": "name",
        "message": "username",
        "color": "color-name",
        "labelColor": "color-name",
        "style": "style-name"
    }
    """
    username = 'lyle'
    colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple', 'grey']
    styles = ['flat', 'plastic', 'flat-square', 'for-the-badge', 'social']

    resp = client.get(f'/api/v1/data?username={username}')
    assert resp.status_code == 200
    returned_data = json.loads(resp.data)
    assert isinstance(returned_data, dict)
    assert returned_data['schemaVersion'] == 1
    assert returned_data['message'] == username
    assert returned_data['label'] == 'name'
    assert returned_data['color'] in colors
    assert returned_data['labelColor'] in colors
    assert returned_data['style'] in styles


def test_json_endpoint_bad_http_method(client):
    """Tests that the json route returns method not allowed message on POST request.

    GIVEN we have the /api/v1/data?username=username route
    WHEN we send a POST request
    THEN we should get a 405 error code in the response
    """
    resp = client.post('/api/v1/data?username=lyle')
    assert resp.status_code == 405


def test_json_endpoint_no_name(client):
    """Tests that the json route returns bad request when name is missing.

    GIVEN we have the /api/v1/data route
    WHEN we send a GET request with no name
    THEN we should get a 400 error code in the response
    """
    resp = client.get('/api/v1/data')
    assert resp.status_code == 400
