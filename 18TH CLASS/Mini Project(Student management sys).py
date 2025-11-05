student=[]
def add_student():
    name=input('Enter Student Name :')
    age=int(input('Enter The Age : '))
    marks=int(input ('Enter The Marks'))
    grade=input('enter The grade')
    
    student.append(name,age,marks,age,)
    print('Student',name, 'added succesfully')

def search_student():
    roll=input('Enter Roll Number To search : ')
    for i in range:
        if i['roll'] == roll:
            print(f'Found :{i}')
            print('The Student Not Found')


def delete_student():
    roll=input('enter The troll number to delete')
    for i in range:
        if i['roll']==roll:
            student.remove(i)
            print('record Deleted !')
        else:
            print('student not found')

def main():
    while True:
        print('=====Student Managment System======')
        print('1. Add student')
        print('2. View Student')
        print('3.Search Strudent')
        print('4. Update Student')
        print('5. Delete student')
        print('6.Exit')

        choice=input('Enter Your Choice')

        if choice =='1':
            add_student()
        elif choice==2:
            print('hy')
            # view_student()
        elif choice ==3:
           search_student()
        elif choice == 4:
            print('hy')
            # update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print('Good bye !!!')
            break
        
if __name__=='__main__':
    main()
