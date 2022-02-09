import json

with open('data.json', encoding='utf-8') as f:
    info = json.load(f)
    print(info)
