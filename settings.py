import os

class Settings:
    GITHUB_ENDPOINT = "https://api.github.com"
    GITHUB_USER = os.getenv("GITHUB_USER")
    GITHUB_EMAIL = os.getenv("GITHUB_EMAIL")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


s = Settings()
