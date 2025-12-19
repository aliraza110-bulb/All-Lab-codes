import pandas as pd

data=[45,5,545,6,9]
my_series=pd.Series(data)
print(my_series)

print("---------------------------------------------")

data=[45,5,'jhon',True,9]
my_series=pd.Series(data)
print(my_series)

#we can store any value 

print("---------------------------------------------")

data = [10, 20, 30, 40, 50]

# create a series from the list
my_series = pd.Series(data)

# display third value in the series
print(my_series[2])



print("---------------------------------------------")



data=[45,5,9]
my_series=pd.Series(data,index=["x","y","z"]) #By this method we can do our custom indexing 
print(my_series)

print("---------------------------------------------")

grades={"chemistry":'43',"english":'60',"computer":'60'}
my_series=pd.Series(grades)
print(my_series)


print("---------------------------------------------")
#by dicitionary
data={"name":['ali','baqer','qasim'],
      "age":['16','18','15'],
      "city":['karachi','j.t','b.area']}
df=pd.DataFrame(data)
print(df)

print("---------------------------------------------")


#by 2d list
data1=[['ali','baqer','qasim'],
      ['16','18','15'],
      ['karachi','j.t','b.area']]
df1=pd.DataFrame(data1,columns=['name','age','city'])
print(df1)


print("---------------------------------------------")

df2 = pd.read_csv('/home/steampup-qbh/Desktop/ALI RAZA (X-A)/All-Lab-codes/27TH CLASS/test.csv')
print(df2)


print("---------------------------------------------")
#how to create empty dat frame
df3=pd.DataFrame()
print(df3)

print("---------------------------------------------")

df4=pd.DataFrame(data)
df.to_csv('data.csv',index=False)


print("---------------------------------------------")


df.set_index('name',inplace=True)
print(df)




print("---------------------------------------------")
print()

print("orginal Data frame")
print(df)
print()

#renaming
df.rename(index={0:'A',1:'B',2:'C'},inplace=True)


print('Modified DataFrame')
print(df)



print("---------------------------------------------")
print()

#ranging 

df=pd.DataFrame(data,index=pd.RangeIndex(5,8,name='index'))
print(df)



print("---------------------------------------------")
print()


df.iloc[1]
print(df.iloc[1])


print("---------------------------------------------")
print()

print(df.index)
print(df.index.values)