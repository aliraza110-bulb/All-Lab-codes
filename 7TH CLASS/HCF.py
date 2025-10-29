def compute_hcf(x, y):
   while(y):
      x , y = y , x % y
   return x
x = int (input("Enter The  Value : "))
y = int (input('Enter The Value : '))

hcf = compute_hcf(x,y)
print("The HCF is", hcf) 