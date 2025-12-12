class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def study(self):
        print(self.name,"IS Studying")


class teacher(person):
    def study(self):
        print(self.name,"IS Studying")
    def role (self):
        print("Teaching conduct the class")

class monitor(student,teacher):
    def manage(self):
        print(self.name,"Is managing class")

def describe_role(obj):
    obj.role()
describe_role(student("kamran"))
describe_role(teacher("kamran"))



