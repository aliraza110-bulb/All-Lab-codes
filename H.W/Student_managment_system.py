# You are designing a Student Attendance Management System for a university class. The
# system should:
#  Allow the user (professor) to add the names of students who attended class today.
#  If the professor accidentally adds the same student&#39;s name more than once, the system
# should remove that student&#39;s name from the attendance list (undoing the entry).
#  After the professor is done entering the names, the system will display the final
# attendance list.
# Explanation of the Code:
# 1. Empty Attendance List:
#  We initialize an empty list attendance_list to keep track of the students who
# attended.
# 2. Taking Attendance:
#  The professor is prompted to enter student names one by one.
#  If a name is already in the list (entered by mistake again), the system removes the name,
# effectively &quot;undoing&quot; the entry.
#  If the name is not already in the list, it adds the student’s name.
# 3. Stopping Condition:
#  The professor can stop entering names by typing &#39;done&#39;.
# 4. Final Attendance List:
#  After all names are entered, the system displays the final list of students who attended
# class.
#  If the list is empty (due to errors or removal), it shows &quot;No students were marked as
# # present.&quot;

attendence_list=[]
while True:
    name=input('Enter The Name Of Student or type (finish) for final list :')
    if name=='finish':
        print("The Final List Of Students")
        print(attendence_list)
        


    if name in attendence_list:
        attendence_list.remove(name)
        print(f"{name} Has Been Removed Becuase It Is Duplicate")
    else:
        attendence_list.append(name)
        print(f"The {name} Has Been Added Sucessfully")
    

