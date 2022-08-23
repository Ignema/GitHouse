from .collection import Collection
from settings import s
from lib.web import *

class Database:
    def __init__(self, name: str):
        self.name = name

    def create(self):
        res = post("/user/repos", data={"name": self.name, "auto_init": True})
        if res.status_code == 422:
            raise Exception("Database already exists")
        return res.json()

    def delete(self):
        res = delete(f"/repos/{s.GITHUB_USER}/{self.name}")
        if res.status_code == 403:
            raise Exception("Not authorized to delete repository")
        return res.json()

    def get_collections(self):
        branchs = get(f"/repos/{s.GITHUB_USER}/{self.name}/git/refs/heads")
        return [Collection(branch["ref"].split("/")[-1], self.name) for branch in branchs]

    def get_collection(self, collection_name):
        return Collection(collection_name, self.name)

    def create_collection(self, collection_name):
        collection = Collection(collection_name, self.name)
        try:
            collection.create()
        except Exception:
            pass
        finally:
            return collection

    def delete_collection(self, collection_name):
        return Collection(collection_name, self.name).delete()