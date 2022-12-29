import server
from server import app
import pytest


class TestPointsShowSummary:
    client = app.test_client()

    competition = [
        {
            "name": "new test",
            "date": "2023-03-27 10:00:00",
            "numberOfPlaces": "22"
        }
    ]
    club = [
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

    def test_show_summary_club_points_update(self, load_data):
        points_before = int(self.club[0]["points"])
        purchased_places = 5

        self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                  "club": self.club[0]['name'],
                                                  "places": purchased_places})

        result = self.client.post('/showSummary', data={"email": self.club[0]['email']})

        assert result.status_code == 200
        assert f"Points available: {points_before - purchased_places}" in result.data.decode()
