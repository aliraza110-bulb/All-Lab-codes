class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def show(self):
        print("Name : ",self.name,"Salary : ",self.__salary)

emp = employee("jessa",10000)
print("name",emp.name,"Salary",emp.employee__salary)

emp.show()