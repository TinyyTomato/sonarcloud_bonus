import json
import os

file_size = os.path.getsize("8.json")

with open("8.json", "r") as file:
    json_data =  json.load(file)
print(json_data["issues"])

print(len(json_data))
