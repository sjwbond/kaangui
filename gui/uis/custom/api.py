from copy import deepcopy
import requests
import json
import zlib
import hashlib
import os

os.environ["NO_PROXY"] = "localhost"

class WebAPI:
  def __init__(self, api_path: str, user_id: str):
    self.api_path = api_path
    self.user_id = user_id

  def list_models(self) -> list[dict]:
    req = requests.get(f"{self.api_path}/models")
    return req.json()

  def get_model(self, id: str) -> dict:
    req = requests.get(f"{self.api_path}/models/{id}")
    metadata = req.json()
    filereq = requests.get(f"{self.api_path}/files/{metadata['hash']}")
    model = self.decompress_model(filereq.content)
    return model | metadata

  def get_model_history(self, id: str) -> list[dict]:
    req = requests.get(f"{self.api_path}/models/history/{id}")
    return req.json()

  def get_model_version(self, version_id: str) -> dict:
    req = requests.get(f"{self.api_path}/models/version/{version_id}")
    metadata = req.json()
    filereq = requests.get(f"{self.api_path}/files/{metadata['hash']}")
    model = self.decompress_model(filereq.content)
    return model | metadata

  def create_model(self, model: dict) -> str:
    stripped = self.strip_model(model)
    compressed = self.compress_model(stripped)
    req = requests.post(f"{self.api_path}/files", files={"model": ("model", compressed)})
    res = req.json()
    metadata = {
      "name": model["name"],
      "hash": res["hash"],
      "user_id": self.user_id
    }
    req = requests.post(f"{self.api_path}/models", json=metadata)
    return (req.json()["modelId"], res["hash"])

  def update_model(self, id: str, model: dict) -> str:
    stripped = self.strip_model(model)
    compressed = self.compress_model(stripped)
    req = requests.post(f"{self.api_path}/files", files={"model": ("model", compressed)})
    res = req.json()
    metadata = {
      "name": model["name"],
      "hash": res["hash"],
      "user_id": self.user_id
    }
    requests.put(f"{self.api_path}/models/{id}", json=metadata)
    return res["hash"]

  def delete_model(self, id: str) -> None:
    requests.delete(f"{self.api_path}/models/{id}")

  def send_model_to_processing(self, name: str, hash: str, priority: int):
    data = {
      "name": name,
      "hash": hash,
      "priority": priority,
      "user_id": self.user_id
    }
    requests.post(f"{self.api_path}/jobs", json=data)

  def strip_model(self, model: dict) -> dict:
    new_model = deepcopy(model)
    new_model.pop("name", None)
    new_model.pop("hash", None)
    new_model.pop("id", None)
    new_model.pop("_id", None)
    new_model.pop("modelId", None)
    new_model.pop("versionId", None)
    new_model.pop("savedByName", None)
    return new_model

  def compress_model(self, model: dict) -> bytes:
    data_json = json.dumps(model)
    data_encoded = data_json.encode("utf-8")
    data_compressed = zlib.compress(data_encoded)
    return data_compressed

  def decompress_model(self, data_compressed: bytes) -> dict:
    data_encoded = zlib.decompress(data_compressed)
    data_json = data_encoded.decode("utf-8")
    model = json.loads(data_json)
    return model

  def hash_bytes(self, bytes: bytes) -> str:
    m = hashlib.sha256()
    m.update(bytes)
    return m.hexdigest()

  def list_results(self) -> list[dict]:
    req = requests.get(f"{self.api_path}/results")
    return req.json()

  def list_tsn_for_result(self, name: str) -> list[dict]:
    req = requests.get(f"{self.api_path}/results/{name}")
    return req.json()

  def get_time_series_data(self, queries: list[dict]) -> list[dict]:
    req = requests.post(f"{self.api_path}/results/time_series_data", json=queries)
    return req.json()
