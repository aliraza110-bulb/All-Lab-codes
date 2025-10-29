#attendenc_list
attendence_list=[]

while True:
    name=input("Enter The Name Of Student (Type 'stop' to end ) : ")
    if name.lower=='stop':
        break 
    if name in attendence_list:
        attendence_list.remove(name)
        print(f'{name} Is Duplicate So It has Been Removed') 
    else:
        attendence_list.append(name)
        print(f'{name} Is Added Succesfully In List')
if ('\nFinal Attendence List In Alphabatical Order Is:'):
    print(attendence_list)
    attendence_list.sorted(name)


   