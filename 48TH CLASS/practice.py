import numpy as np
import pandas as pd 

data=np.array([
    ["IT",50000],
    ["HR",-45000],
    ["Finance",60000],
    ["IT",70000]
])

df=pd.DataFrame(data, columns=["dept","salary"])
df["salary"]=pd.to_numeric(df["salary"])

df=df[df["salary"]>0]

df["Normalized_salary"]=(df["salary"]-df["salary"].mean())/ df["salary"].std()

print(df)

print("\nRandom Sample:\n",df.iloc[1])
print(df.groupby('dept')["salary"].mean())