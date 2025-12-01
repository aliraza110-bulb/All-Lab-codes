import matplotlib.pyplot as plt
import  seaborn as sns

df=sns.load_dataset("tips")

print(df.head)
print('\n')
# sns.jointplot(x="total_bill",y="tip",data=df,kind="scatter")

# plt.show()

# sns.jointplot(x="total_bill",y="tip",data=df,kind="reg")

# plt.show()

# sns.jointplot(x="total_bill",y="tip",data=df,kind="hex")

# plt.show()

# sns.jointplot(x="total_bill",y="tip",data=df,kind="kde")

# plt.show()

# sns.displot(df["total_bill"],kde=False)
# plt.show()

# sns.pairplot(df,hue='sex')
# plt.show()

sns.rugplot(df["total_bill"],color='black')
plt.show()
