# a=1/0
# print(a)


# y=a+5

# a=[1,2,3]
# a[10]

# try:
#     a=1/0
#     print(a)
# except:
#     print('there Was An error')

# try:
#     y=a+5
#     print(y)

# except:
#     print('there was an error')


x=1
try:
    y= int(input('please enter a number to divide a :'))
    x=x/y
    print('success  a=',y)

except ZeroDivisionError:
    print('num can not divide by 0')
except ValueError:
    print('You did not provide a number')
except:
    print('Something went wrong')

else:    print("success a=",y)

finally:
    print('processing complete')



# def safe_divide(a,b):
#         a=int(input('Enter The 1 value'))
#         b=int(input('Enter The 2 value'))
#     try:
#         result=a/b
#         return result
#     except ZeroDivisionError:
#         print('Error: CAnnot divide by zero')
#         return None
# return(safe_divide(a,b))







import math



def sqaure_root(number1):
    try:
        sqrt=math.sqrt(number1)
        print('The square root is :',sqrt)
    except ValueError:
        print('Invalid input! Please enter a float or integer number and positive value.')
while True:
    number1=float(input('Enter The Value Of Number :'))
    print(sqaure_root(number1))
    exit_choice=('type exit to stop else enter')
    if exit_choice == 'exit':
        break
    
def complex_calc(num):
    try:
        result=num/(num-5)
        print("the value after dividing is",result)
    except Exception:
        print("An error occured during calculation")
while True:
        num=int('enter The Value Of Num')
        print(complex_calc(num))
        exit_choice=('type exit to stop else enter')
        if exit_choice == 'exit':
            break


