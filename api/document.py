import base64
import collections.abc
from settings import s
from lib.web import *

class Document:
    def __init__(self, name: str, path: str, value: str, database: str, collection: str):
        self.name = name
        self.value = value
        self.path = path
        self.database = database
        self.collection = collection

    def create(self):
        res = put(f"/repos/{s.GITHUB_USER}/{self.database}/contents/{self.path}{self.name}", data={"message": f"add {self.name}","committer":{"name": s.GITHUB_USER, "email": s.GITHUB_EMAIL}, "content": base64.b64encode(self.value.encode('utf-8')).decode("utf-8"), "branch": self.collection})
        if res.status_code == 422:
            raise Exception("Document already exists")
        return res.json()

    def delete(self):
        try:
            res = delete(f"/repos/{s.GITHUB_USER}/{self.database}/contents/{self.path}{self.name}", data={"message": f"delete {self.name}", "committer":{"name": s.GITHUB_USER, "email": s.GITHUB_EMAIL},"sha": get_sha(), "branch": self.collection})
        except Exception as e:
            raise Exception("Error in fetching document")
        if res.status_code == 403:
            raise Exception("Not authorized to delete repository")
        return res.json()

    def get_sha(self):
        file = get(f"/repos/{s.GITHUB_USER}/{self.database}/contents/{self.path}{self.name}?ref={self.collection}")
        if file.status_code == 404:
            raise Exception("Resource not found")
        elif isinstance(file.json(), collections.abc.Sequence):
            raise Exception("Not a single document")
        return file.json()["sha"]
