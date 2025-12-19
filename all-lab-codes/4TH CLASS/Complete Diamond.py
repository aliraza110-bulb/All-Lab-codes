n=int(input("Enter The Number :"))
<<<<<<< HEAD
for i in range(5, n + 1):
=======
for i in range(1, n + 1):
>>>>>>> 1184928beb89a58c4029b6ac5eaa87c95f5069e1
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
