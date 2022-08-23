from client import Client
from api.database import Database

def main():
    client = Client()
    db = client.create_database("cookie")
    strawberry = db.create_collection("strawberry")
    strawberry.create_document("strawberry.txt", "", "strawberry")

if __name__ == "__main__":
    main()
