from locust import HttpUser, task
from server import loadClubs, loadCompetitions


class LocustTestPerformance(HttpUser):
    clubs = loadClubs()
    competitions = loadCompetitions()

    def on_start(self):
        self.client.get("/", name="index")
        self.client.post("/showSummary", data={"email": self.clubs[0]["email"]}, name="login")

    @task
    def book_places(self):
        self.client.get(f"/book/{self.competitions[0]['name']}/{self.clubs[0]['name']}", name="book")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", data={"club": self.clubs[0]["name"],
                                                  "competition": self.competitions[0]["name"],
                                                  "places": 1},
                         name="purchase_places"
                         )

    @task
    def show_clubs_points(self):
        self.client.get("/showClubsPoints", name="clubs_points")
