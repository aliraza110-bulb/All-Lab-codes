list=['java','ruby','c++']
print("\n List Of Numbers : ")
print(list[0])
print(list[2])
print(list)
print(len(list))

list=[['java'],['c+', 'ruby']]
print(list[1][0])
print([1] [0])

string=(input("enter elements(space separated):"))
lst=string.split()
print("the list is: ",lst)


# n=int(input("Enter The Size Of List "))
# lst=list(map(int,input("enter The Integer Elements: )").strip().split()))[n:]
# print("the list is ",lst)

list=['java','c']
for i in range(1,4):
   list.append(i)
   print("\n list after addition of elements from 1-3: " )
   print(list)

list2 = ['ruby','java']
list.append(list2)
print("\n list after addition of : ")
print(list)


list2 = ['ruby','java']
list.insert(3,12)
print("\n list after addition of : ")
print(list)