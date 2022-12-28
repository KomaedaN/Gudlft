import server
import pytest
from server import app


class TestBook:
    client = app.test_client()
    competition = [{"name": "Spring Festival", "date": "2023-03-27 10:00:00", "numberOfPlaces": "25"},
                   {"name": "Test competition", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"}]
    club = [{"name": "Simply Lift", "email": "test@simplylift.co", "points": "10"}]

    @pytest.fixture
    def load_data(self, request):
        server.competitions = self.competition
        server.clubs = self.club

    def test_book_found_club_competition(self, load_data):
        result = self.client.get(f'/book/{self.competition[0]["name"]}/{self.club[0]["name"]}')

        assert result.status_code == 200

    def test_book_found_past_competition(self, load_data):
        result = self.client.get(f'/book/{self.competition[1]["name"]}/{self.club[0]["name"]}')

        assert result.status_code == 200
        assert "This competition is over you can&#39;t purchase places" in result.data.decode()

