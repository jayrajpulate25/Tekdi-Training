# JSON Practice
# Baseline Course

import json

# Create a dictionary to convert to JSON
data = {
    "name": "Jayraj",
    "age": 22,
    "is_student": False,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "Paud Road",
        "city": "Pune",
        "zip_code": "411038"
    }
}

# Convert dictionary to JSON string
json_string = json.dumps(data, indent=4)
print("JSON String:")
print(json_string)

# Save JSON to a file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
print("\nData has been written to 'data.json'.")

# Read JSON from a file
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("\nLoaded Data from 'data.json':")
    print(loaded_data)

# Access specific data
print("\nAccessing specific data:")
print(f"Name: {loaded_data['name']}")
print(f"City: {loaded_data['address']['city']}")


# JSON string with an array of objects

json_array = '''
[
    {"id": 1, "name": "Demo1", "role": "Developer"},
    {"id": 2, "name": "Demo2", "role": "Designer"},
    {"id": 3, "name": "Demo3", "role": "Manager"}
]
'''

# Parse JSON string into Python list
data = json.loads(json_array)

# Loop through the list and print details
print("Employees:")
for employee in data:
    print(f"ID: {employee['id']}, Name: {employee['name']}, Role: {employee['role']}")

