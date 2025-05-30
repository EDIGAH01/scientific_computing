import numpy as np
from scipy.integrate import dblquad

# Define the function
def func(y, x):
    return x**2 + y**2

# Calculate the volume using double integration
volume, error = dblquad(func, 0, 1, lambda x: 0, lambda x: 1)
print(f"Volume under the surface: {volume:.4f}")