from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client['test']
        self.collection = self.client['testCol']
        print(self.db.list_collection_names())


if __name__ == "__main__":
    db = Database()