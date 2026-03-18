import json

users = [
    {"name": "Amit", "age": 28},
    {"name": "Priya", "age": 25},
    {"name": "Rahul", "age": 31}
]
adult_user = []

for user in users:
    if user['age'] > 26:
        adult_user.append(user)

with open("user.json", "w") as file:
    json.dump(adult_user, file,indent=4)

with open("user.json", "r") as file:
    j_users= json.load(file)

for u in j_users:
    print(u['name'])

