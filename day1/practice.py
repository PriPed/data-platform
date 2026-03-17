import json
import csv
import requests



users = [
  {"name": "Amit", "age": 28},
    {"name": "Priya", "age": 22},
    {"name": "Rahul", "age": 31},
    {"name": "Neha", "age": 24}
]

#================================================================
# return user who's age is more than 25

for user in users:
    if user['age']>25:
        print(user['name'])

#=================================================================
#get the count of user who's age is more than 25

total = 0
for user in users:
    if user['age']>25:
        total =total+1

print(total)

#===================================================================
#Add a new field "is_adult".

#Rules:

#age >= 18 → True
#age < 18 → False

for user in users:
    if user["age"] > 25:
        user['is_adult'] = True
    else:
        user['is_adult'] = False
print(users)

#===========================================================================
#Python script should:

#Load JSON

#Print all names

with open("user.json", "r") as file:
    data = json.load(file)
print(data)

for  d in data:
    print(d["name"])

#==============================================================

# Using the same data.
# Task:Save processed users into:

processed_users= []
for d in data:
    processed_users.append({
        "name": d['name'],
        "age": d["age"]
    })
  
with open("output.json", 'w') as file:
    json.dump(processed_users, file, indent=4)


#===============================================================

#read and print csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    print(reader)

    for cd in reader:
     print(f"{cd['name']} earns {cd['salary']}")
     if int(cd['salary']) > 55000:
         print(cd['name'])

#===================================================================

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
users = response.json()

for user in users:
    print(user['name'])


#===================================================================

orders = [
    {"user": "Amit", "amount": 200},
    {"user": "Priya", "amount": 300},
    {"user": "Amit", "amount": 150}
]

totals = {}

for o in orders:
   user = o["user"]
   amount = o["amount"]

   if user not in totals:
     totals[user] = 0

   totals[user] += amount
print(totals)

for user,total  in totals.items():
         print(user, "->" , total)


   





  








    


        



