import pandas as pd




print("---------------------------------------------\n")
print()

data={"name":['ali','baqer','qasim','abdullah','raza'],
      "age":['16','18','15','17','15'],
      "city":['karachi','j.t','b.area','j.t','karachi',]}
df=pd.DataFrame(data)
print(df)



print("---------------------------------------------\n")
print()

print("First Five Row")
print(df.head())


print("---------------------------------------------\n")
print()


print("Last Five Row")
print(df.tail())


print("---------------------------------------------\n")
print()

address = ['abc','newyork','malir','usa','karachi']  # 5 items
df["address"] = address

print(df.info())



print("---------------------------------------------\n")
print()

df.loc[len(df.index)]=['ali',27,"karachi","korangi"]
print(df)


print("---------------------------------------------\n")
print()

#remove rows
print("Original rows")
print(df)
df.drop(index=2,inplace=True)


print("Modified rows")
print(df)

#remove columns

print("Original columns")
df.drop(columns='age',inplace=True)
print("Modified columns")
print(df)

print("---------------------------------------------\n")
print()

#DUPLicate entry
print(df.duplicated())


print("---------------------------------------------\n")
print()



