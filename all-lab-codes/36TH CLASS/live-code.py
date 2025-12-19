raw= " Age: 21yrs , Hieght : 5.8ft , weight = 65 kg "

clean=raw.replace(" ","").lower()


age=int(clean[clean.index("age:")+4 : clean.index("yrs")])
hieght=float(clean[clean.index("hieght:")+7 : clean.index("ft")])
weight=int(clean[clean.index("weight=")+7 : clean.index("kg")])
temp=int(clean[clean.index("Temp : ")+7 : clean.index("C")])
Humidity=int(clean[clean.index("Humidity = ")+11 : clean.index("%")])

print(age,hieght,weight)

temp_float=float(temp)
humidity_float=float(Humidity)
age_float=float(age)
height_int=int(hieght)
weight_flaot=float(weight)

print(age_float,height_int,weight_flaot,humidity_float,temp_float)

raw=raw+"Temp : 38C , Humidity =85%"