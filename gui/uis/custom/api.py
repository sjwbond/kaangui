import requests

API_PATH = "http://localhost:3000"

def list_models():
  req = requests.get(f"{API_PATH}/models")
  return req.json()

def get_model(id):
  req = requests.get(f"{API_PATH}/models/{id}")
  return req.json()

def create_model(model):
  req = requests.post(f"{API_PATH}/models", json=model)
  return req.json()["id"]

def update_model(id, model):
  req = requests.put(f"{API_PATH}/models/{id}", json=model)

def delete_model(id):
  req = requests.delete(f"{API_PATH}/models/{id}")
