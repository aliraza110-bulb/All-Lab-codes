import pandas as pd
import numpy as np

data = {
    'Name': ['baqer', 'ALi raza', 'Abdullah', 'Hussain'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['Karachi', 'Lahore', None, 'Quetta']
    
    }

print(data)
 
bonus=pd.Series([5,10,7,8],index=data.index)

data=data.fillna(data.mean())
data=data.add(bonus,axis=0)

data["Total"]=data.sum(axis=1)
data["average"]=data["Name","Science"].mean(axis=1)

print(data)
print("\n failed Students\n",data[data["average"]<75])

print(data["Total "].indexmax())
print(data.fillna(data.median()))