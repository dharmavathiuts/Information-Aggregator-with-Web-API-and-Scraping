import requests
import json

class NewsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def fetch_news(self, category=None, country='us'):
        params = {
            'apiKey': self.api_key,
            'category': category,
            'country': country
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        if data.get('status') == 'error':
            raise Exception(f"API Error: {data.get('message')}")
        return data