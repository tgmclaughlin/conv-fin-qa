import json
from pathlib import Path


def load_data():
    data_file = Path(__file__).parent.parent.parent / "./dataset/first_train_entry.json"
    with open(data_file, "r") as file:
        return json.load(file)
