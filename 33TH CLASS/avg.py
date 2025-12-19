marks = list(map(int, input("Enter Marks Separated By Space: ").split()))
avg=sum(marks)/len(marks)

print("Average Marks:",avg)
print("Highest Marks",max(marks))
print("Lowest Marks",min(marks))

avg_list=[]

for m in marks:
    if m>avg:
        avg_list.append(m)
        if avg_list:
         print("Following Are The Students That Scored Marks Greater Than Average:",m)
        else:
         print("Not Found")