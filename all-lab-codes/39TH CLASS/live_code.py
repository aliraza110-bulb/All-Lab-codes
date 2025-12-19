data = "BP:120/80 HR=72% Temp=38.9C Sugar -155mg Chol=190mg HDL=45mg LDL=110mg"

bp= data[data.index("BP:")+3 : data.index("HR")].strip()
systolic, diastolic = [int(x) for x in bp.replace ("HR","").split("/") ]

hr_str= data[data.index("HR=")+3 : data.index("%")]
hr= int(hr_str)

temp_str=data[data.index("Temp=")+5 : data.index("C")]
temp=float(temp_str)

sugar=int(data[data.index("Sugar -")+6 : data.index("mg")])

Chol=int(data[data.index("Chol=")+5 : data.index("mg")])

print(systolic,diastolic,hr,temp,sugar,Chol)

