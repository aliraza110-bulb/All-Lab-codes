def add(a,b):
    b=a+b    
    print(a,"if you add one", b)
    return(b)


# help(add)

def subtract(a,b):
    b=a-b
    print(a,"if you subtract one", b)
    return(b)


def multiply(a,b):
    b=a*b
    print(a,"if you multiply two", b)
    return(b)



def divide(a,b):
    b=a//b
    print(a,"if you divide 2 then value is ", b)
    return(b)

a=int(input("Enter thye value"))
b=int(input('Enter The Value'))

add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)

