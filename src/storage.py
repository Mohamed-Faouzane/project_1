import json
from models import Student

# Write to file
def save_students(students, filename):
    with open(filename, "w") as f:
        json.dump([{"name": s.name, "grade": s.grade} for s in students], f)

# Read file
def load_students(filename):
    with open(filename, "r") as f:
        loaded = json.load(f)
    return [Student(s["name"], s["grade"]) for s in loaded]

def add_student(filename, name, grade):      
    try:
        students = load_students(filename)
    except FileNotFoundError:
        students = []                                    # Start fresh if file doesn't exist yet
    students.append(Student(name, grade))                # append a Student object, not two args
    save_students(students, filename)

def remove_student(filename, name):
    students = load_students(filename)
    match = [s for s in students if s.name == name]      # find if the student exists. Creates a new list to which all students with their name  same as the entered "name".
    if not match:
        print(f"Student '{name}' not found.")
        return
    students = [s for s in students if s.name != name]   # filter out by name. Creates a new list to which all students with name different from the entered "name".
    save_students(students, filename)
    
