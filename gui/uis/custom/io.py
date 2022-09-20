import json
from typing import Tuple, Union
from pymongo import MongoClient
import gridfs
import requests


# FileSystem
def save_model_to_file(model: dict, filename: str):
    with open(filename, 'w') as fp:
        json.dump(model, fp, sort_keys=True, indent=4)

def load_model_from_file(filename: str) -> Union[Tuple[dict, dict], None]:
    with open(filename, 'r') as f:
        data = json.load(f)
        if "SystemInputs" in data:
            return (data, data["SystemInputs"])
    return None

# MongoDB
def save_model_to_mongodb(model: dict):
    client = MongoClient("127.0.0.1", 27017)
    db = client['DB_Fundamental']
    fs = gridfs.GridFS(db)
    fs.put(model)
