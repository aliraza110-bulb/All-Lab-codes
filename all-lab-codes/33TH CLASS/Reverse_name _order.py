name=input("Enter Your Full Name: ").upper().split()
if len(name)==1:
      print("You Entered Single Name")
else:
   name.reverse()
   print("Name In Reverse Order :",name)
   name1=" ".join(name)
   print("Joined String",name1)