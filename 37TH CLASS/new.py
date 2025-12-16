class Person:
    def __init__(self, name):
        self.name = name

    def role(self):
        print(self.name, "has no specific role")  

class Student(Person):
    def study(self):
        print(self.name, "is studying")

    def role(self): 
        print(self.name, "is a student")

class Teacher(Person):
    def study(self):
        print(self.name, "is studying")

    def role(self):
        print(self.name, "teaches the class")

class Monitor(Student, Teacher):
    def manage(self):
        print(self.name, "is managing the class")

    def role(self): 
        print(self.name, "is a monitor")


def describe_role(obj):
    obj.role()


describe_role(Student("Kamran"))
describe_role(Teacher("Ali"))
describe_role(Monitor("Sara"))

