# a=str(input('Enter The String or Words : '))
# vowels = 'aeouiAIOUE'
# for char in a:
#     if char in vowels:
# #         print(char)

# x=str(input("enter the text"))
# vowels="aeiouAEIOU"
# count=0

# for char in x:
#      if char in vowels:
#        count +=1
#       print('vowel found !', char)

#      print("Number Of vowel:", count)

    
    
    
    
    
    
x = str(input("Enter the text: "))

vowels = "aeiouAEIOU"
count = 0

for char in x:
    if char in vowels:
        count += 1
        print('Vowel found!', char)

print("Number of vowels:", count)
