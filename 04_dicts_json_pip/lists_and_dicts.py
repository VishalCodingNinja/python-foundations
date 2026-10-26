# A list of dictionaries: many records with the same shape
people = [
    {"name": "Ana", "age": 31},
    {"name": "Raj", "age": 27},
]
print(people[1]["name"])  # Raj

for person in people:
    print(person["name"])

# A dictionary of lists: values grouped under a key
grades = {
    "math": [90, 85],
    "art": [70, 95, 88],
}
print(grades["art"][0])   # 70

grades["math"].append(77)
print(grades)
