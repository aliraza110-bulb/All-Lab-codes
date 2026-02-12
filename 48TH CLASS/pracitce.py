import pandas as pd

df=pd.DataFrame({
    'Name':['Ali','sara','jhon','ayesha',"zain","hamza"],
    'department':["It","IT","HR","Finance","HR","CS"],
    'performance':[88,75,90,85,68,92],
    'exprience':[6,4,8,7,3,9]

})

df['weighted score']=(df["performance"]*0.7)+ (df['exprience']*0.3)

df['level'] = pd.cut (
df['weighted score'],
bins=[0,70,85,100],
labels=["needs improvement","good","Excellent"]
)

df['dept_rank'] = df.groupby('department')['weighted score'].rank(ascending=False)

print(df)

top_performer = df [df(df['dept_rank'] == 1) & (df['level'] == 'excellent')]
print("\n Top department performer : \n ", top_performer)

print(df.groupby('department')['weighted score'].mean())
print(df.sort_values('weighted_score',ascening=False))