from datetime import datetime
import json
from typing import Union
from gui.core.json_settings import Settings
from gui.uis.custom.api import WebAPI

settings = Settings()
api = WebAPI(settings.items["api_path"])

def input_int(prompt: str, less_than: int, allow_empty: bool = False) -> Union[int, None]:
    user_input = input(prompt)

    if allow_empty and user_input == "":
        return None

    try:
        user_input = int(user_input)
    except:
        print("Error: Invalid input")
        exit()

    if user_input < 0 or user_input >= less_than:
        print("Error: Index out of range")
        exit()
    
    return user_input

print("Models")
models = api.list_models()
for i in range(len(models)):
    print(f"  {i} - {models[i]['name']}")

model_index = input_int("Select a model: ", len(models))
model = models[model_index]

print()
print("Versions")
versions = api.get_model_history(model["id"])
for i in range(len(versions)):
    date = datetime.fromisoformat(versions[i]['savedAt'][0:-1])
    formattedDate = date.strftime("%d-%m-%Y %H:%M:%S")
    is_current = model["hash"] == versions[i]['hash']
    print(f"  {i} - {formattedDate}{' (current)' if is_current else ''}")

version_index = input_int("Select a version: ", len(versions), True)

full_model = None
if version_index is None:
    full_model = api.get_model(model["id"])
else:
    full_model = api.get_model_version(model["id"], versions[version_index]["id"])

if "name" in full_model:
    del full_model["name"]
if "hash" in full_model:
    del full_model["hash"]
if "id" in full_model:
    del full_model["id"]

print()
file_name = input(f"Output file [{model['name']}.json]:")
if file_name == "":
    file_name = f"{model['name']}.json"

with open(file_name, "w") as out_file:
    json.dump(full_model, out_file, sort_keys=True, indent=4)
