# qestion 1: write a program to find the maximum and  minimum value in a list.    

list=[1,2,3,4,2,2,5,2,6,]
max_value=max(list)
print('The maximum value in list is:',max_value)
min_value=min(list)
print('The minimum value in list is:',min_value)

# quetsion 2: remove duplicate from a list
list_after_removing_same_elements=set(list)
print('------------------------------------------')
print('List after removing duplicate elements:',list_after_removing_same_elements)  
print('------------------------------------------')

# question no 3 :write aprogram to count the occurence of each element in a list
element_count=list.count(list)
print('The occurence of element is : ',element_count)

# question no 4 demonstrate tupple unpacking with an example

tupple1=(1,2,3,4,5,6)
tupple2=(7,8,9,10,11)

after_unpacking=tupple1+tupple2
print('After Unpacking The tupple is found to be :',after_unpacking)

# DICITIONARIES
# qestion no 1 : create a dicionaery of 5 studentwith name as keys and their marks as valuews . print the average marks of the student 
student_marks={'Alice':85,'Bob':90,'Charlie':78,'David':92,'Eva':88}
total_marks=sum(student_marks.values())
average_marks=total_marks/len(student_marks)
print('The average marks of the students is :',average_marks)   

# question no 2 : write a program to add and and remove from dictionary
student_marks['Frank']=80
print('After adding Frank the dictionary is :',student_marks)
del student_marks['Charlie']
print('After removing Charlie the dictionary is :',student_marks)   

