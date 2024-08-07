from bson import ObjectId

from app.core.db import collection


def find_all_ids():
    obj_list = list(collection.find({}, {"_id": 0, "id": 1}))
    return [doc["id"] for doc in obj_list]


def convert_object_id(document):
    if isinstance(document, list):
        # If it's a list, recursively process each item
        return [convert_object_id(item) for item in document]
    elif isinstance(document, dict):
        # If it's a dictionary, recursively process each key-value pair
        return {key: convert_object_id(value) for key, value in document.items()}
    elif isinstance(document, ObjectId):
        # If it's an ObjectId, convert to a string
        return str(document)
    else:
        # Return the document if no conversion is needed
        return document


def get_json_by_id(option_id):
    # Fetch the document by the "id" field
    document = collection.find_one({"id": option_id})
    return convert_object_id(document)
