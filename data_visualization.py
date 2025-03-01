import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.arange(1, 11)  # X-axis values from 1 to 10
y = np.random.randint(1, 100, size=10)  # Y-axis random values between 1 and 100

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Data Line Graph')
plt.legend()
plt.grid()

# Save the plot as an image
plt.savefig('plot.png')
plt.show()
