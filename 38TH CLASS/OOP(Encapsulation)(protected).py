class Company:
    def __init__(self):
        self._project = "NLP"  # protected attribute

class Employee(Company):
    def __init__(self, name, salary):
        super().__init__()        # call parent constructor
        self.name = name
        self.__salary = salary    # private attribute

    def show(self):
        print(f"Name: {self.name}, Salary: {self.__salary}, Project: {self._project}")

# Create object
emp = Employee("Ali", 50000)
emp.show()
