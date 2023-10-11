import random

from locust import HttpUser, between, task


class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def make_prediction(self):
        payload = {
            "PULocationID": random.randint(1, 266),
            "DOLocationID": random.randint(1, 265),
            "passenger_count": random.randint(1, 6),
        }

        self.client.post("/predict", json=payload)
