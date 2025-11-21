odd_square=[]

for x in range(1,21):
    if x%2==1:
        odd_square.append(x**2)

print("Odd Squares :",odd_square)

sum_of_odd_square=sum(odd_square)

print(f"The Sum Of Odd_square Is Found To Be:",sum_of_odd_square)

even_square=[]

for x in range(1,22):
    if x%2==0:
        even_square.append(x**2)

print("even Squares :",even_square)

sum_of_even_square=sum(even_square)

print(f"The Sum Of even_square Is Found To Be:",sum_of_even_square)


sum_of_both=sum_of_even_square+sum_of_odd_square
print("The Sum Of Even Or Odd Square Is Found To Be : ",sum_of_both)