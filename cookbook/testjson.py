import json

data = {

}

with open('/Users/jiawa/PycharmProjects/pythonstudy/cookbook/data.json', 'r') as f:
    data = json.load(f)

print(data['hello'])
