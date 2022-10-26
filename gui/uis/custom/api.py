from copy import deepcopy
import requests
import json
import zlib
import hashlib

API_PATH = "http://localhost:3000"

def list_models() -> list[dict]:
  req = requests.get(f"{API_PATH}/models")
  return req.json()

def get_model(id: str) -> dict:
  req = requests.get(f"{API_PATH}/models/{id}")
  metadata = req.json()
  filereq = requests.get(f"{API_PATH}/models/file/{metadata['hash']}")
  model = decompress_model(filereq.content)
  return model | metadata

def get_model_history(id: str) -> list[dict]:
  req = requests.get(f"{API_PATH}/models/history/{id}")
  return req.json()

def get_model_version(model_id: str, version_id: str) -> dict:
  req = requests.get(f"{API_PATH}/models/version/{version_id}")
  metadata = req.json()
  metadata["id"] = model_id
  filereq = requests.get(f"{API_PATH}/models/file/{metadata['hash']}")
  model = decompress_model(filereq.content)
  return model | metadata

def create_model(model: dict) -> str:
  stripped = strip_model(model)
  compressed = compress_model(stripped)
  req = requests.post(f"{API_PATH}/models/file", files={"model": ("model", compressed)})
  res = req.json()
  metadata = {
    "name": model["name"],
    "hash": res["hash"]
  }
  req = requests.post(f"{API_PATH}/models", json=metadata)
  return req.json()["id"]

def update_model(id: str, model: dict) -> None:
  compressed = compress_model(model)
  req = requests.post(f"{API_PATH}/models/file", files={"model": ("model", compressed)})
  res = req.json()
  metadata = {
    "name": model["name"],
    "hash": res["hash"]
  }
  requests.put(f"{API_PATH}/models/{id}", json=metadata)

def delete_model(id: str) -> None:
  requests.delete(f"{API_PATH}/models/{id}")

def strip_model(model: dict) -> dict:
  new_model = deepcopy(model)
  model.pop("name", None)
  model.pop("hash", None)
  model.pop("id", None)
  model.pop("_id", None)
  return new_model

def compress_model(model: dict) -> bytes:
  data_json = json.dumps(model)
  data_encoded = data_json.encode("utf-8")
  data_compressed = zlib.compress(data_encoded)
  return data_compressed

def decompress_model(data_compressed: bytes) -> dict:
  data_encoded = zlib.decompress(data_compressed)
  data_json = data_encoded.decode("utf-8")
  model = json.loads(data_json)
  return model

def hash_bytes(bytes: bytes) -> str:
  m = hashlib.sha256()
  m.update(bytes)
  return m.hexdigest()
