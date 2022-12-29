import server
import pytest
from server import app


class TestDisplayClubPoints:
    client = app.test_client()

    def test_display_club_points(self):
        result = self.client.get('/showClubsPoints')

        assert result.status_code == 200
