# LAB 1(Comment)

#This Is Single Line Comment

"""This is multi line comment"""

print("\n")

#LAB 2(If-Else Condition)

no=int(input("Enter The Number : "))

if no > 0:
    print("No is Postitive")
else:
    print("No is Negative")

print("\n")

#LAB 3 (Lists)

list=[]

name=input("Enter Your Name : ")
list.append(name)
print("The Name Is",name)


print("\n")

#LAB 4 (Sets)

set={1,2,3,4}
print(set)
set.add(4)
print(set)


print("\n")

#LAB 5 (String Slicing)

str="ali","abdullah","baqer"
print("The Orginal String",str)
print("This Print String On 0 Index",str[0],"\n","This Prints String On 1 Index",str[1],"\n")
print("This Reverse The String",str[::-1])


print("\n")

#LAB 6 (Functions)

def greet():
    print("Hello Friends")
greet()


print("\n")

#LAB 9 (Regex)

import re

text=" hy wifi password is 112 643"

nums=re.findall(r'\d+',text)
print("Its Print Two Or More Digits From Text",nums)


print("\n")

#LAB 10 (numpy)

import numpy as np
arr=np.array([1,2,3,4])
print("Numpy Array",arr)

print("\n")

#LAB 11 (Matplotlib)

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[4,5,6,7])
plt.show()


arr=np.array([1,2,35])
print(arr)

plt.plot([1,235],[34,65,67])
plt.show()