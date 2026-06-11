import os
import argparse
from models import Student
from storage import load_students, add_student, remove_student

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(BASE_DIR, "grades_cli.json")

parser = argparse.ArgumentParser(description = "Student grade manager")
subparsers = parser.add_subparsers(dest = "command")

# "add" command - takes name and grade
add_parser = subparsers.add_parser("add")
add_parser.add_argument("name")
add_parser.add_argument("grade", type = int)

# "list" command - takes nothing
subparsers.add_parser("list")

# "remove" command - takes name
remove_parser = subparsers.add_parser("remove")
remove_parser.add_argument("name")

args = parser.parse_args()
if args.command == "add":
    add_student(DB_FILE, args.name, args.grade)
    print(f"Added '{args.name}' with grade {args.grade}")               # See what gets parsed
elif args.command == "list":
    students = load_students(DB_FILE)
    students.sort()
    for s in students:
        print(f"{s.name} ~ {s.grade}")
elif args.command == "remove":
    remove_student(DB_FILE, args.name)
    print(f"Removed {args.name}")