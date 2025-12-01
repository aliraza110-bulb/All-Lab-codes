def fun():
    print("welcome To The QBHS")
fun()


def add(num1 ,  num2):
    num3=num1+num2
    return num3

num1, num2=5,10
ans = add(num1,num2)
print(f"the addition of {num1} and {num2} results{ans}.")

def evenorodd(x):
  if(x%2 == 0):
    print('The Number Is Even')
  else:
    print('The Number Is Odd')

evenorodd(7)
evenorodd(10)

def fun(x , y=50):
   print('x',x)
   print('y',y)

   fun(10)
   fun(10,5)

def student(firstname, lastname ):
   print(firstname, lastname) 

student(firstname='ali', lastname='Raza')
student(firstname='ahmed',lastname='baqer')

def nameAge(name,age):
   print('hi , I am' , name)
   print('My age is ', age)


print('case 1:')
nameAge('Ali Raza','16')


def square(number):
   return number **2      



results = square(5)
print(results)


def f1():
   s = 'My Name Is Ali Raza'

   def f2():
      print(s)
   f2()

f1()

def factorial (n):
   if n<0:
      return ' error ! factorial of negative number not exist '
   elif n==0:
      return 1
   else :
      return n * factorial(n-1) 


result =  factorial(5)
print(result)

def fibonacci(n):
   if n<0:
       return n 
   else:
      return fibonacci (n-1)
   
results = fibonacci(6)
print(results)

def calculate_total(prices,discount_rate,tax_rate,total_amount):
   total_price=sum(prices)
   print('If you item you have worth more than 1000 you will get 20% discount')
   
     if total_price >1000:

      discount=total_price-discount_rate
      tax_rate=total_price*tax_rate
   else:
      discount_rate=0
      discount=total_price-discount
      tax_rate=total_price*tax_rate


print("The Total Price After Tax And Discount Is",total_amount)

