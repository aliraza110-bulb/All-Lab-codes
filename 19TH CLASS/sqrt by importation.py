import math

def sqaure_root(number1):
    try:
        sqrt=math.sqrt(number1)
        print('The square root is :',sqrt)
    except ValueError:
        print('Invalid input! Please enter a float or integer number and positive value.')
while True:
    number1=float(input('Enter The Value Of Number To Take Square Root :'))
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


