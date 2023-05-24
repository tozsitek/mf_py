import csv

"""with open("students.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        name, house = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        print(f"{name} is in {house}") """
        
## Sorted version
students = []

# sort by the sentence
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
        
for student in sorted(students):
    print(student)
 """ 
 
# sort by a field, either name or house
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # add a dict.
        student = {"name": name, "house": house}
        students.append(student)
        
def get_name(student):
    return student["name"]
# passing in a function as a paramater
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")"""
    
# use lambda instead of a function (unanimous function)
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(
        student = {"name": name, "house": house}
        students.append(student)
 
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")  """
    
    
# use the csv package reader
"""with open("students.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")"""
    
# use csv package dict reader
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})
        # students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
