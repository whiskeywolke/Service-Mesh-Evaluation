# inspired by https://github.com/GoogleCloudPlatform/microservices-demo/blob/main/src/loadgenerator/locustfile.py

import random
from locust import HttpUser, TaskSet, between


def index(l):
    l.client.get("/productpage")

def login(l):
    l.client.post("/login", {
        'username': 'username',
        'passwd': 'password'})

class UserBehavior(TaskSet):
    def on_start(self):
        index(self)

    tasks = {index: 10,
            login: 2}

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)