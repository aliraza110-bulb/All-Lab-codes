import pandas as pd
import matplotlib.pyplot as plt

data = {
    'car': ['Toyota', 'Honda', 'BMW', 'Audi', 'Ford'],
    'weight': [1200, 1100, 1500, 1400, 1300]
}

df = pd.DataFrame(data)

# Line plot
df.plot(
    x='car',
    y='weight',
    kind='bar',
    # marker='o',         # adds circles on data points
    color='blue',
    title='Car Weights' # adds a title
)

plt.xlabel('Car')       # X-axis label
plt.ylabel('Weight (kg)') # Y-axis label
plt.title("car weightage")        # Adds a grid
plt.tight_layout() # if we remove it the half text from bottom get removed or cutted
plt.show()              # Display the plot


