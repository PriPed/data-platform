
#variables
name = "Priya"
age= 25
salry = 50000
is_active = True


print(type(age))

#data types

name = "Priya"
print(name.upper())
print(name.lower())

#interger 

a= 10
b= 3

print(a+b)
print(a%b)


#Boolean

is_logged_in = True
print(is_logged_in)


#lists

numbers = [1,2,3,4,5]
print(numbers[0])
numbers.append(6)
print(numbers)

for n in numbers:
    print(n)


#dictionaries
    user = {
    "name": "Priya",
    "age": 25,
    "city": "Mumbai"
}
    

print(user["name"])
user["salary"] = 50000

print(user)


#conditions

age=20
if age> 18:
   print("Adult")
else:
    print("Minor")


#loops
for i in range(5):
    print(i)

#loops through dictionary

user = {"name": "priya", "age": 25}

for key,value in user.items():
    print(key,value)


#functions

def greet(name):
    return "Hello " + name

print(greet("neha"))


#working with files

with open("data.txt", "w") as file:
    file.write("hello python")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)


#exception handling

try:
    x= 10/100
except ZeroDivisionError:
    print("cannot divide by zero")


#importing modules

import math
print(math.sqrt(16))


#classes

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello", self.name)
        print("hello", self.age)

u1= User("Priya", 25)
u1.greet()





