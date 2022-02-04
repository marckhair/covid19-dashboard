import json
import requests
from datetime import datetime, timedelta

class CovidApi:
    def __init__(self):
        # today: yyyy-mm-dd
        self.today = datetime.now().strftime("%Y-%m-%d")
        # yesterday: yyyy-mm-dd
        self.yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        return None

    def worldwide_summary(self):
        response = requests.get("https://api.covid19api.com/summary")
        return json.loads(response.text)

    # Use this function to get the daily cases of a country. ex: country_daily('Canada')
    def country_daily(self, country):
        response = requests.get("https://api.covid19api.com/country/{c}/status/confirmed?from={y}T00:00:00Z&to={t}T00:00:00Z".format(c = country, y = self.yesterday, t = self.today))
        return json.loads(response.text)