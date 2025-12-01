d = "ABCDEFG"


print(d[0:3])

e="clorkstd"
print(e[::2])
 
print(r"//")

print(d.find("C"))

print(d.replace ("C" , "c"))

a = 5
print(a==6)

i=2

print(i!=6) #it is true i is not equal to 6 

age =18
if age > 18:
    print('You Can Enter')
else:
    print('Go See Meat Loaf')

print('Move On')

age =18
if age > 18:
    print('You Can Use Youtube')
elif age==18:
    print('Go Use Youtube Kids')
else:
  print('Acess Denied')
  
  print('Move On')

album_year = 1980

if(album_year>1979) and (album_year<1990):
    print("The album_year is between 1980 and 1989")

    print("")
    print("Do Stuff...")



ach=7

player_name = "messi"
sports= 'footballer'

if ach>10:
    print("the name of player is:" , player_name ,"The sport he plays is" , sports)
else:
    print(player_name , "Doesnot Have Achivements More Than 10")


ach=20
player="roger"
sports="tennis"

if (ach==20) and (sports=="tennis"):
    print(player,'Play', sports," And Has 20 Achievements Succesfully")
else:
    print(player,"Donot Have 20 Achievemnets")



ach=9
player="ali"
sports="footbal"

if (ach<10) and (sports!="tennis"):
    print(player,'Play', sports," And Has Achievements less than 10 Succesfully")
else:
    print(player,"have Achievemnets greater than 10")






dates = [1983,1980,1973]
N=len(dates)

for i in range(N):
    print(dates[i])





date= [1983,1980,1973]
i=0
year = date[0]

while(year!=1973):
    print(year)
    i=i+1
    year=dates[i]

    print("It Tooks", i , 'repettion to get out of loop.') 




for i in range (-5,6):
    print(i)



genres=['rock','R&B','SoundTrack', 'R&B',"soul",'pop']
n=len(genres)

for i in range(n):
    print(genres[i])



#another way 
  


for e in genres:
    print(e)



playlistRating=[10,9.5,10,8,7.5,5,10,10]
i=0

rating=playlistRating[0]

while(rating>=6):
    print(rating)
    i=i+1
    rating=playlistRating[i]
    print(i)

squares=['orange','orange','purple','blue','orange']
new_square=[]
i=0
while(i<len(squares)and squares[i]=='orange'):
    new_square.append(squares[i])
    i=i+1
    print(new_square)
    