def test_home(client):
    resp = client.get('/api/v1')
    assert resp.status_code == 200


def test_home_bad_http_method(client):
    resp = client.post('/api/v1')
    assert resp.status_code == 405
