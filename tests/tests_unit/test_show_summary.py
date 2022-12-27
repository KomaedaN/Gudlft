"""from server import app
import pytest


@pytest.fixture
def client(request):
    client = app.test_client()

    return client


def test_show_summary(client):
    club = [
        {
            "name": "Test name",
            "email": "john@simplylift.co",
            "points": "10"
        }
    ]

    result = client.post('/showSummary', data=dict(email=f"{club[0]['email']}"))

    assert result.status_code == 200"""
