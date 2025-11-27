import matplotlib.pyplot as plt

x=[3,1,3]
y=[3,2,1]

plt.plot(x,y)
plt.title("line Chart")
plt.legend("Line")
plt.show()

plt.bar(x,y)
plt.title("bar Chart")
plt.legend("bar")
plt.show()

plt.hist(x,bins=5)
plt.title("hist Chart")
plt.legend("hist")
plt.show()

plt.pie(x)
plt.title("pie Chart")
plt.legend("pie")
plt.show()

plt.scatter(x,y)
plt.title("scatter Chart")
plt.legend("scatter")
plt.show()
