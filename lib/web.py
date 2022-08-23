import os
import requests
import json
from settings import s

def get(url: str) -> dict:
    headers = {"Authorization": f"Bearer {s.GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    return requests.get(s.GITHUB_ENDPOINT + url, headers=headers)

def post(url: str, data: dict) -> dict:
    headers = {"Authorization": f"Bearer {s.GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    return requests.post(s.GITHUB_ENDPOINT + url, headers=headers, data=json.dumps(data))

def put(url: str, data: dict) -> dict:
    headers = {"Authorization": f"Bearer {s.GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    return requests.put(s.GITHUB_ENDPOINT + url, headers=headers, data=json.dumps(data))

def delete(url: str, data: dict = {}) -> dict:
    headers = {"Authorization": f"Bearer {s.GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    return requests.delete(s.GITHUB_ENDPOINT + url, headers=headers, data=json.dumps(data))