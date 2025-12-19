import seaborn as sns 
import matplotlib.pyplot as plt

data=sns.load_dataset("iris")

print(data)
plt.figure(figsize=(2,4))
sns.lineplot(x="sepal_length",y="sepal_width",data=data)

plt.xlim(5)
plt.ylim(2)

plt.title("title using matplotlib")
sns.despine()
palette=sns.color_palette()
sns.palplot(palette)
plt.show()