def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        return None


# Get input from user
a = int(input('Enter the first value: '))
b = int(input('Enter the second value: '))

# Call the function
result = safe_divide(a, b)

if result is not None:
    print("Result:", result)
