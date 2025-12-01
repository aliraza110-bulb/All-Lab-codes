value=int(input("Enter"))
value1=int(input("Enter"))

try:
    a=value1/value
    print("The final Results",a)
except ZeroDivisionError:
    print("Cannot Divide By Zero")
except TypeError:
    print("The Type is string or other")