import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
products = ['Product A', 'Product B', 'Product C']

sales_data = pd.DataFrame({
    'Month': np.tile(months, 3),
    'Product': np.repeat(products, len(months)),
    'Sales': np.random.randint(50, 200, len(months)*len(products)),
    'Profit': np.random.randint(10, 100, len(months)*len(products))
})

sns.set_style("whitegrid")

# Create larger figure
fig, axes = plt.subplots(3, 2, figsize=(20, 24))
fig.suptitle("Full Sales Dashboard", fontsize=28)

# Line Chart
sns.lineplot(x='Month', y='Sales', hue='Product', marker='o', data=sales_data, ax=axes[0,0])
axes[0,0].set_title("Monthly Sales Trend", fontsize=14)

# Bar Chart
total_sales = sales_data.groupby('Product')['Sales'].sum().reset_index()
sns.barplot(x='Product', y='Sales', data=total_sales, palette='pastel', ax=axes[0,1])
axes[0,1].set_title("Total Sales per Product", fontsize=14)

# Histogram
sns.histplot(sales_data['Profit'], bins=8, kde=True, color='orange', ax=axes[1,0])
axes[1,0].set_title("Profit Distribution", fontsize=14)

# Scatter Plot
sns.scatterplot(x='Sales', y='Profit', hue='Product', data=sales_data, s=100, ax=axes[1,1])
axes[1,1].set_title("Sales vs Profit", fontsize=14)

# Pie Chart
axes[2,0].pie(total_sales['Sales'], labels=total_sales['Product'], autopct='%1.1f%%', 
              colors=['#FF9999','#66B2FF','#99FF99'], startangle=90)
axes[2,0].set_title("Sales Distribution by Product", fontsize=14)

# Box Plot
sns.boxplot(x='Product', y='Profit', data=sales_data, palette='pastel', ax=axes[2,1])
axes[2,1].set_title("Profit Distribution per Product", fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
products = ['Product A', 'Product B', 'Product C']

sales_data = pd.DataFrame({
    'Month': np.tile(months, 3),
    'Product': np.repeat(products, len(months)),
    'Sales': np.random.randint(50, 200, len(months)*len(products)),
    'Profit': np.random.randint(10, 100, len(months)*len(products))
})

sns.set_style("whitegrid")

fig, axes = plt.subplots(3, 2, figsize=(18, 18))
fig.suptitle("Full Sales Dashboard", fontsize=24)

sns.lineplot(x='Month', y='Sales', hue='Product', marker='o', data=sales_data, ax=axes[0,0])
axes[0,0].set_title("Monthly Sales Trend")

total_sales = sales_data.groupby('Product')['Sales'].sum().reset_index()
sns.barplot(x='Product', y='Sales', data=total_sales, palette='pastel', ax=axes[0,1])
axes[0,1].set_title("Total Sales per Product")

sns.histplot(sales_data['Profit'], bins=8, kde=True, color='orange', ax=axes[1,0])
axes[1,0].set_title("Profit Distribution")

sns.scatterplot(x='Sales', y='Profit', hue='Product', data=sales_data, s=100, ax=axes[1,1])
axes[1,1].set_title("Sales vs Profit")

axes[2,0].pie(total_sales['Sales'], labels=total_sales['Product'], autopct='%1.1f%%', colors=['#FF9999','#66B2FF','#99FF99'])
axes[2,0].set_title("Sales Distribution by Product")

sns.boxplot(x='Product', y='Profit', data=sales_data, palette='pastel', ax=axes[2,1])
axes[2,1].set_title("Profit Distribution per Product")

plt.tight_layout()
plt.show()
