import json


computers = [
    {
        'id': 1,
        'name': 'Asus',
        'color': 'Black'
    },
    {
        'id': 2,
        'name': 'Victus',
        'color': 'Grey'
    },
    {
        'id': 3,
        'name': 'HP',
        'colo': 'White'
    },
    {
        'id': 4,
        'name': 'Lenovo',
        'color': 'Red'
    }
]

with open("computers.json", "w") as f:
    json.dump(computers[0:], f)

print(json.dumps(computers))