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





