import csv
import json
import logging

users = []
def parse_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None
    
def read_csv(filename):
  
    with open(filename, "r") as file:
        # csv_data = file.read()
        reader = csv.DictReader(file)
        for row in reader:
           age = parse_int(row['age'])
           if age is None:
                logging.warning(f"Invalid age in row: {row}")
           users.append(row)
    return users    

def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

            
read_csv("new_data.csv")
save_json(users, "output.json")