code = "PRD2025-BT77-CAT-XL"
allowed_size={"X","S","M","L","XL","XS"}
version="VER-1.9.3"

Year=code[3:7]
batch=code[8:11]
category=code.split("-")[2]
size=code[-2:]

if size in allowed_size:
    print("The Size Is Valid")
else:
    print("Size Is Not Valid")


print("Year :",Year,"\ncategory :",category,"\nsize :",size,"\nbatch code :",batch)




