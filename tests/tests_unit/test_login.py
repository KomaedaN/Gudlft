from server import app


def test_login():
    client = app.test_client()
    result = client.get("/")
    assert result.status_code == 200


def test_signup():
    client = app.test_client()
    result = client.get("/logout")
    assert result.status_code == 302
