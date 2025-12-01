a=float(input("Enter The First Number : "))
b=float(input("Enter The Second Number : "))
#ask which operation you want to perform
print("Which Operation You Want To Perform")
A=print("1=Add")
B=print("2=Subtraction")
C=print(" 3=Multiplication")
D=print("4=Divison")

print("________________________________________choose any Operation _______________________________________")
c=int(input(""))
if c == 1:
  print(a+b)
elif c == 2:
  print(a-b)
elif c == 3:
  print(a*b)
elif c == 4:
  print(a/b)
else:
  print("You Chosen Invalid Operator")