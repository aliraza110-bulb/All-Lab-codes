n=int(input("Enter The Number"))
for i in range(1, n + 1):
   for j in range(n, i - 1, -1):
      print(" ", end="")
   for k in range (1, i + 1):
      print("*", end="")
   for l in range(2, i + 1):
      print("*", end="")
   print()

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(n, i - 1, -1):
        print("*", end="")
    for l in range(n - 1, i - 1, -1):
        print("*", end="")
    print()