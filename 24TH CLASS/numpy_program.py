import numpy as np

# 10 rows, 7 columns, random temperatures between 25 and 50
temperature_random = 25 + (50 - 25) * np.random.rand(10, 7)

print("Random Temperature Array (10x7):")
print(temperature_random)

# Average temperature
avg_temp = np.mean(temperature_random)
print("\nAverage Temperature:", avg_temp)
