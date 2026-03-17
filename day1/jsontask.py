import json
import requests
# Write a Python script that: Reads the JSON file and Prints each user's name

with open("user.json", "r") as file:
    users = json.load(file)
    for user in users:
        print(user['name'])

#==============================================================================


# Task 2 — Filter JSON Data Using the same JSON.

# Task:Print users whose age > 27

    for user in users:
        if user['age'] > 27:
            print(user['name'])


#================================================================================

#Task 3 — Modify JSON Data
#Add a new field: "is_adult": True
#Rule: age >= 18 → True

for user in users:
        if user['age'] > 18:
           user['is_adult'] = True
        else:
           user['is_adult'] = False
           
print(users)

#=======================================================================

#Task 4 — Add New User

#Write a script that:Reads users.json Adds a new user: {"name": "Neha", "age": 24, "city": "Bangalore"}
#  Saves the updated JSON file.

with open("user.json", "r") as file:
    users = json.load(file)
    new_user = {
    "name": "Neha",
    "age": 24,
    "city": "Bangalore"
    }
    users.append(new_user)

# with open("user.json", "w") as file:
    # json.dump(users,file,indent=4)

#====================================================================

#Task 5 — Count Users by City

#From the JSON data. Create output like:

# Mumbai → 1
# Delhi → 1
# Pune → 1

with open("user.json", "r") as file:
    users = json.load(file)

totals = {}

for user in users:
    city = user['city']

    if city not in totals:
        totals[city] = 0
    totals[city] +=1

for user,total in totals.items():
    print(user , "->", total)

#====================================================================

#     Task 6 — Convert JSON to Another Format

# From the JSON file create a new file:

# names.json

# Containing only names:

# ["Amit", "Priya", "Rahul"]

names = []

with open("user.json", "r") as file:
    users = json.load(file)

    for user in users:
        names.append(user['name'])


with open ("names.json", "w") as file:
    json.dump(names,file,indent=4)


#===================================================================================]
# Task 7 — Sort JSON

# Sort users by age (descending).

# Expected output:

# Rahul - 31
# Amit - 28
# Priya - 25

users_sorted = sorted(users, key=lambda user:user['age'], reverse=True)

for user in users_sorted:
    print(user['name'] , "->", user['age'])

#==========================================================================

with open("user.json", "r") as file:
    users = json.load(file)

grouped = {}

for user in users:
    city = user["city"]
    name = user["name"]

    if city not in grouped:
        grouped[city] = []

    grouped[city].append(name)

print(grouped)

#==============================================================================


        





















