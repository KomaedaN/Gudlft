import server
from server import app
import pytest


class TestPurchasePlacesWithoutPoints:
    client = app.test_client()

    competition = [
        {
            "name": "new test",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "22"
        },
        {
            "name": "test",
            "date": "2024-03-27 10:00:00",
            "numberOfPlaces": "10"
        }
    ]
    club = [
        {
            "name": "New",
            "email": "test@simplylift.co",
            "points": "2"
        },
        {
            "name": "test club points",
            "email": "test@gmail.com",
            "points": "10"
        }
    ]

    @pytest.fixture
    def load_data(self, request):
        server.competitions = self.competition
        server.clubs = self.club

    def test_purchase_places_without_points(self, load_data):
        self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                  "club": self.club[0]['name'], "places": 2})

        result = self.client.post('/purchasePlaces', data={"competition": self.competition[1]['name'],
                                                           "club": self.club[0]['name'], "places": 2})

        assert result.status_code == 200
        assert "You need more points" in result.data.decode()
