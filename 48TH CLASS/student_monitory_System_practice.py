import pandas as pd
import numpy as np

marks=np.array([
    [88,92,85,99,87],
    [65,60,58,62,64],
    [75,78,72,70,74],
    [95,94,96,93,97],
    [55,52,50,48,54],
    [82,88,78,85,83]
])

students=["ali","murtaza","Danish","messaum","ali","Baqer"]
subjects=['math','physics','chemisrty','computer','english']

df=pd.DataFrame(marks, index=students,columns=subjects)

df['total']=df.sum(axis=1)
df['percentage'] = (df['total']/500)*100

df['gpa']=df['percentage']/25

df['status']=df['gpa'].apply(
    lambda x: 'deans list' if x >= 3.7 else
    'normal standing ' if x >= 2.5 else 
    'probation'
    )

print(df)

print("\n Student on probation : \n", df[df["status"]=='probation'])
print("\n Category count : \n", df['status'].value_counts())