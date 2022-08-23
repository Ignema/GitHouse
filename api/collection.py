from .document import Document
from settings import s
from lib.web import *

class Collection:
    def __init__(self, name: str, database: str):
        self.database = database
        self.name = name
    
    def create(self):
        branchs = get(f"/repos/{s.GITHUB_USER}/{self.database}/git/refs/heads").json()
        for branch in branchs:
            if branch["ref"] == "refs/heads/main":
                sha = branch["object"]["sha"]
                res = post(f"/repos/{s.GITHUB_USER}/{self.database}/git/refs", data={"ref": f"refs/heads/{self.name}", "sha": sha})
                if res.status_code == 422:
                    raise Exception("Collection already exists")
                return res.json()
        raise Exception("No main branch found")

    def delete(self):
        res = delete(f"/repos/{s.GITHUB_USER}/{self.database}/git/refs/heads/{self.name}")
        if res.status_code == 403:
            raise Exception("Not authorized to delete repository")
        return res.json()

    def get_all_documents(self):
        return get_item("")

    def get_document(self, path: str):
        res = get(f"/repos/{s.GITHUB_USER}/{self.name}/contents/{path}")
        if res.status_code == 404:
            raise Exception("Resource not found")
        return res.json()

    def create_document(self, name: str, path: str, content: str):
        return Document(name, path, content, self.database, self.name).create()