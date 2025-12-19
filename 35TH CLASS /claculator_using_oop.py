class calculator:
    def __init__(self,a,b,value):
        self.value=value
        self.a=a
        self.b=b
    def add(self):
        self.value=self.a+self.b
        return self.value
    def subtract(self):
        self.value=self.a-self.b
        return self.value
    def multiplication(self):
        self.value=self.a*self.b
        return self.value
    def division(self):
        self.value=self.a/self.b
        return self.value
while True:

    print("1.add,2.subtract,3.multiplication,4.division")
    choice=int(input("Enter The Choice"))
    a=int(input("Enter Value Of First Number"))
    b=int(input("Enter The Value Of second Number"))

    calc=calculator(a,b,value=0)


    if choice == 1:
        print(calc.add())
    elif choice == 2:
        print(calc.subtract())
    elif choice == 3:
        print(calc.multiplication())
    elif choice == 4:
        print(calc.division())

    else:
        print("Error")