import server
from server import app
import pytest


class TestPurchasePlaces:
    client = app.test_client()

    competition = [{"name": "new test", "date": "2023-03-27 10:00:00", "numberOfPlaces": "25"}]
    club = [{"name": "New", "email": "test@simplylift.co", "points": "7"}]

    @pytest.fixture
    def load_data(self, request):
        server.competitions = self.competition
        server.clubs = self.club

    def test_purchase_places_0(self, load_data):
        result = self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                           "club": self.club[0]['name'], "places": 0})
        assert "You can&#39;t select 0 or less places" in result.data.decode()

    def test_purchase_places_valid(self, load_data):
        result = self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                           "club": self.club[0]['name'], "places": 1})

        assert "Great-booking complete!" in result.data.decode()

    def test_purchase_places_more_12(self, load_data):
        result = self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                           "club": self.club[0]['name'], "places": 13})

        assert "You can&#39;t purchase more then 12 places" in result.data.decode()

    def test_purchase_places_error(self, load_data):
        result = self.client.post('/purchasePlaces', data={"competition": self.competition[0]['name'],
                                                           "club": self.club[0]['name'], "places": 10})
        assert "You need more points" in result.data.decode()
