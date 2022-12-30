from locust import HttpUser, task
from server import loadClubs, loadCompetitions


class LocustTestPerformance(HttpUser):
    clubs = loadClubs()
    competitions = loadCompetitions()

    def login(self):
        self.client.get("/")
        self.client.post("/showSummary", data={"email": self.clubs[0]["email"]})

    @task
    def book_places(self):
        self.client.get(f"/book/{self.competitions[0]['name']}/{self.clubs[0]['email']}")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces", data={"club": self.clubs[0]["name"],
                                                  "competition": self.competitions[0]["name"],
                                                  "places": 1}
                         )
