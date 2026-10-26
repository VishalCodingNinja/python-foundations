import json
from pathlib import Path

text = '{"name": "Ana", "langs": ["Python", "SQL"]}'
data = json.loads(text)       # str -> dict
print(data["langs"][0])       # Python

back = json.dumps(data)       # dict -> str
print(back)

# Read the JSON file that sits next to this script
json_file = Path(__file__).parent / "contacts.json"
with open(json_file, encoding="utf-8") as f:
    contacts = json.load(f)   # file -> dict

for name, info in contacts.items():
    print(name, info["phone"])
