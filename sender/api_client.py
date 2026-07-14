import json
import requests
from config.config import API_GATEWAY_URL, API_KEY


class APIClient:
    def __init__(self, url: str = API_GATEWAY_URL, api_key: str = API_KEY):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

    def send_payload(self, payload: dict) -> requests.Response:
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload), timeout=30)
        response.raise_for_status()
        return response
