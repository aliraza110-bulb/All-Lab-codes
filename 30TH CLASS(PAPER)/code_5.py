dict={}

dict1=list(dict)
def insert_student():
    name=str(input("enter The studentr name "))
    dict1.append(name)
    print("added")
    
def remove_student():
    rem=str(input("enter The name of student to remove"))
    if rem in dict1:
        dict1.remove(rem)
        print(rem,"removed")
    else:
        print("name Not Found")

def update_student():
    updates=str(input("Enter The Name to Update"))
    dict.update(updates)
    print("The Updated Dict is ",dict)

# def search_student():
#     search=str(input("enter Teh name to search"))
#     for i in range

# def main():
#     choose=input()


# if __name__=='__main__':
#     main()

insert_student()
remove_student()
update_student()