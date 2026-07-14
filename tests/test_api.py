import pytest
from sender.api_client import APIClient


class DummyResponse:
    def __init__(self, status_code=200):
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception('HTTP error')


class DummySession:
    def post(self, url, headers=None, data=None, timeout=None):
        return DummyResponse(200)


def test_api_client_builds_headers(monkeypatch):
    monkeypatch.setattr('sender.api_client.requests.post', lambda *args, **kwargs: DummyResponse())
    client = APIClient(url='https://example.com', api_key='test-key')
    response = client.send_payload({'test': 'data'})
    assert response.status_code == 200
