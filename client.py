import os
from api.database import Database

class Client:
    def __init__(self, credentials: dict = {}):
        if isinstance(credentials, dict) and "user" in credentials and "email" in credentials and "token" in credentials:
            self.credentials = credentials
        else:
            self.credentials = {}
            self.credentials["user"] = os.getenv("GITHUB_USER")
            self.credentials["email"] = os.getenv("GITHUB_USER")
            self.credentials["token"] = os.getenv("GITHUB_USER")

    def create_database(self, name):
        database = Database(name)
        try:
            database.create()
        except Exception:
            pass
        finally:
            return database