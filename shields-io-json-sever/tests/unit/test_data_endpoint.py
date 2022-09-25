import json

def test_shields_io_data(client):
    expected_data = {
        "schemaVersion": 1,
        "label": "name",
        "message": "lyle okoth",
        "color": "green"
    }

    resp = client.get('/api/v1/data/1')
    assert resp.status_code == 200
    # returned_data = json.loads(resp.data)
    # assert type(returned_data) is dict 
    # assert returned_data == expected_data