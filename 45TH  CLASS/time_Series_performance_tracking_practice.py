import pandas as pd

df=pd.DataFrame({
    "Score":[70,56,80]

},index=["Jan","feb","March"])

df["growth"]=df["Score"].diff()

print(df)
print("\nPerformance drop\n",df[df["growth"]<10])
print("\n March score",df.loc["March"])

print("\n Highest Month With Score",df["Score"].idxmax())