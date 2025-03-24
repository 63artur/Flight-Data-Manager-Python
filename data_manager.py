import requests
from dotenv import load_dotenv
class DataManager:
    def __init__(self):
        self.data = requests.get("https://api.sheety.co/a0a65cb588aebc4503f03369b57086fc/flightDeals/prices")
        self.data = self.data.json()
        self.data = self.data["prices"]
