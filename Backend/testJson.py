import json

with open('outputProxyCurl.json', 'r') as file:
        data = json.load(file)

print(data[0])