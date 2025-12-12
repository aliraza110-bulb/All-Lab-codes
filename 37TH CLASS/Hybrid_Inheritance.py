class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def study(self):
        print(self.name,"IS Studying")


class teacher(person):
    def teacher(self):
        print(self.name,"Is Teaching")

class monitor(teacher):
    def monitor(self):
        print(self.name,"Is Managing Class")