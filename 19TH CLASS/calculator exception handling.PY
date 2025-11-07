try:
    print("Simple Calculator with Exception Handling")
    a = float(input("Enter The First Number: "))
    b = float(input("Enter The Second Number: "))

    
    print("\nWhich Operation You Want To Perform:")
    print("1 = Add")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("________________________________________")

    c = int(input("Choose any operation (1-4): "))

    if c == 1:
        print("Result:", a + b)
    elif c == 2:
        print("Result:", a - b)
    elif c == 3:
        print("Result:", a * b)
    elif c == 4:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        print("Result:", a / b)
    else:
        raise ValueError("Invalid operation selected! Choose between 1 and 4.")

except ValueError as ve:
    print("Error:", ve)

except ZeroDivisionError as zd:
    print("Error:", zd)

except Exception as e:
    print("Unexpected Error:", e)

