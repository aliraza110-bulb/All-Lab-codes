print("Hello World")
#print the tradational hello world

z=15+2
print({z})

#n=(input("Enter Any Number"))
print(type(90.989))
print(int(12.23))
#this  gives error
#int('1 or 2 people')

print(str(1.2))
print(type(False))

# use // for answer in int or use / for answer in float
n=(6//2)
print(n)
print(type(n))

#applying condition answer will be false type will be boolean
n=("hello"== "world")
print(n)
print(type("hello" == "world"))

#1001 is in string convert in integer
n="1001"
print(type(n))
print(int(n))


x=43+60+16+41
print(x)
b=x/60
print(b)

#you can also use '' for string and can use "" for string

name = ('ALI RAZA')
print(name[0])
'''
len stands for 
'''


len('Ali Raza')

print(name[0:4])

print(name[::2])

print(name[0:4:5])

a=(input('Enter The Name'))
# upper case combination , replacing combination, and adding like any name like than is good boy or ...
state= a.upper() + "is a good boy".upper()
print(state)
b = state.replace('good'.upper(),'bad').upper()
print(b)




# replacing way janet instead of ali raza x-a
a="ali raza x-a"
b= a.replace('ali raza x-a', 'janet')
print(b)


name = 'the body guard'
print(name.find('guard'))

import re
s1 = "ali raza"

#define pattern for search
pattern = r"raz"

result =re.search(pattern, s1)

# check found or not
if result:
    print("Match Found !")
else :
    print("Match Not Found.")