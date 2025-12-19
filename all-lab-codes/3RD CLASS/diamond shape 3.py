n=int(input("Enter The First Number"))
for i in range (1, n + 1 ):
    for j in range(1, i+1):
        print("*",end="")
    print()

for i in range(1,n+1):
    for space in range(n-1):
        print(" ",end="")
    for i in range(i,n+1):
        print("*")
        print()
   


for i in range (1, n+1 ):
    for j in range(n+1-i):
        print(" ",end="")
    print()


