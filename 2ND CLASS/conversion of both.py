print("what do you want to do")
print("KM TO MILES = 1")
print("MILES TO  KM = 2")

choice=int(input("Enter Your Choice (1 or 2):"))
if choice == 1:
  n = float(input("input the distance in km_"))
  d = n*0.621371
  n = print(f"The {n} is {d} Miles")
 
elif choice == 2:
  n = float(input("input the distance in Miles_"))
  d = n/0.621371
  n = print(f"The {n} is {d} km")

else:

 ("invalid choice ! (choose 1 or 2)")