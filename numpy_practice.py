# import numpy as np
# # Create a 1D array

# array_1d = np.array([1, 2, 3, 4, 5])
# print("1D Array:")
# print(array_1d)

# # Create a 2D array
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print("\n2D Array:")
# print(array_2d)

# # Create a 3D array
# array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print("\n3D Array:")
# print(array_3d)



# Common NumPy Operations
#Sum, mean, max, min

from asyncio import locks

import numpy as np

# sales = np.array([500, 600, 400, 850, 900])

# print(sales.sum())    # Total: 3250
# print(sales.mean())   # Average: 650.0
# print(sales.max())    # Highest: 900
# print(sales.min())    # Lowest: 400




# Array Arithmetic
# One of the most powerful features of NumPy is that you can perform operations on an entire array at once, without writing a loop.
# numbs = np.array([5, 10, 15, 20, 25])
# print(numbs * 3)     # Output: [15 30 45 60 75]




# Boolean Filtering
# NumPy allows you to filter data based on conditions. This is called boolean indexing. It is very useful for tasks like finding which students passed an exam.

# students = np.array([85, 92, 78, 96, 88])
# passed = students >= 80
# print("Students who passed:")
# print(students[passed])




# Shape and Reshape
# The shape of an array tells you how many rows and columns it has. Reshape allows you to change the structure of an array without changing its data.

# final_studentscores = np.array([50, 70, 30, 65, 35, 10, 90])

# # Check shape
# print(final_studentscores.shape)   # Output: (7,)  means 7 elements, 1D

# # Reshape to 4 rows x 2 columns (only works if total elements match)
# scores_8 = np.array([50, 70, 30, 65, 35, 10, 90, 80])
# reshaped = scores_8.reshape(4, 2)
# print(reshaped)



# Random Number Generation with NumPy
# NumPy has its own random module that is more powerful than Python's built-in random module. It is commonly used in machine learning to generate sample data.


# import numpy as np

# # Generate 5 random integers between 1 and 100
# print(np.random.randint(1, 100, size=5))

# # Set a seed so results are reproducible
# np.random.seed(101)
# print(np.random.randint(1, 100, size=5))




# Class Tasks Summary (NumPy)
# These are the tasks completed in class:

# Task 1: Create an array of 5 numbers and multiply by 3
# numbs = np.array([5, 10, 15, 20, 25])
# print(numbs)       # [5 10 15 20 25]
# numbs * 3          # array([15, 30, 45, 60, 75])
# print(numbs * 3)   # [15 30 45 60 75]

# # Task 2: Create a 2x2 matrix and print its shape
# mat = np.array([[3, 4], [6, 7]])
# print(mat.shape)

# # Task 3: Given scores [50, 60, 30, 90, 20], find average, highest, and lowest
# scores = np.array([50, 60, 30, 90, 20])
# print(scores.mean())   # 50.0
# print(scores.max())    # 90
# print(scores.min())    # 20

# # Task 4: Generate 5 random integers between 1 and 100
# np.random.randint(1, 100, size=5)
# # array([21, 32, 19, 1, 59], dtype=int32)
# print(np.random.randint(1, 100, size=5))

