
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __lt__(self, other):
        return self.grade > other.grade
