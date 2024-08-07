import json

import mongomock

client = mongomock.MongoClient()
db = client['mongo']
collection = db['convfinqa']


def load_data(filepath: str):
    with open(filepath, 'r') as file:
        data = json.load(file)
        collection.insert_many(data)


load_data('./dataset/train.json')
