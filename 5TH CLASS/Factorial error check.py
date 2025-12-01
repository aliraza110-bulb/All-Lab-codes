def factorial(num):
    if num ==1:
        return num
    else:
      return num * factorial (num-1)
num = int(input("Enter The Number : "))
if num < 0:
     print ("factorial cannot be found for negative number")
elif num ==1:
    print("factorial of 0 is 1")
else:
   print("factorial at" ,"num, is:" ,factorial(num))