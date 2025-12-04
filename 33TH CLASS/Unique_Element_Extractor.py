numbers=[1,2,2,3,4,4,5]
unique_number=[]

for num in numbers:
    if num not in unique_number:
        unique_number.append(num)

        print("Unique Numbers :",unique_number)

#By Using sets

numbers={1,2,2,3,4,4,5}
unique_number={}

for num in numbers:
    if num not in unique_number:
        unique_number.append(num)

        print("Unique Numbers :",unique_number)


        #Sorting descending

descending=sorted(unique_number,reverse=True)
print("Unique Numbers In Descending Order",descending)

count=len(unique_number)

