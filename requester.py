import requests
from Directions import Directions

class Requester:
    def __init__(self):
        self.URL = "http://localhost:8080"
        self.PARAMS = {'direction':'forward'}

    def send(self, command, params):
        print(params)
        response = requests.get(url = self.URL+command, params = params)
        print(response.json())
        return response