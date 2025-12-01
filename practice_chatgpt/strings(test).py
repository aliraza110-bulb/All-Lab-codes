string="Hello World Hy"
print(string[0])
print(string[4])

print(string[6:11])

#for Revrse 
print(string[::-1])

#vowel

string=input("enter the Text")
count=0
vowels="aeiouAEIOU"
for char in string:
    if char in vowels:
        count+=1
        print(count)

#to print middle three character
string = "teacher"
if len(string) % 2 == 1:
    mid = len(string) // 2
    print(string[mid-1:mid+2])
else:
    print("Not valid")
