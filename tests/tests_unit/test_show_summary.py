from server import app
import pytest
import server


class TestShowSummary:
    client = app.test_client()

    club = [{"name": "Test club", "email": "test@simplylift.co", "points": "7"}]

    @pytest.fixture
    def load_data(self, request):
        server.clubs = self.club

    def test_show_summary(self, load_data):
        result = self.client.post('/showSummary', data=dict(email=f"{self.club[0]['email']}"))

        assert result.status_code == 200

    def test_show_summary_invalid_email(self, load_data):
        result = self.client.post('/showSummary', data=dict(email="test@gmail.com"))

        assert result.status_code == 200
        assert "This email is not valid please try again" in result.data.decode()
