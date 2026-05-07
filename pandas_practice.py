# import numpy as np
# import pandas as pd

# # Pandas Series
# # A Series is a one-dimensional array-like object that can hold any data type. It is
# # similar to a list or an array, but it has additional features like indexing and labels.
# # student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
# # CA1_scores = [85, 90, 78, 92, 88]
# # CA2_scores = [80, 95, 82, 88, 91]
# # CA3_scores = [90, 85, 88, 91, 87]
# # Exam_scores = [92, 88, 90, 94, 89]

# # s1 = pd.Series(CA1_scores)
# # print(s1.sum())




# # Creating a DataFrame from a Dictionary

# # What is a Dictionary?
# # Before even getting to Pandas, you need to understand what the curly braces {} mean. A dictionary is a Python data structure that stores data in key and value pairs. Think of it like a real dictionary where a word is the key and the definition is the value.

# # import numpy as np
# # import pandas as pd

# # scores = {
# #     'Math':    [90, np.nan, 70],
# #     'Science': [85, np.nan, np.nan],
# #     'English': [95, 85, 75]
# # }

# # df = pd.DataFrame(scores, index=['Alice', 'Bob', 'Charlie'])
# # print(df)
# # Note: np.nan stands for 'Not a Number'. It represents a missing value. You will often encounter missing data in real-world datasets.
# # pd.DataFrame() takes your dictionary and converts it into a table. Each key becomes a column header. Each list becomes the column's data. The index gives each row a label, in this case the student names.




# # Random DataFrames with NumPy
# # You can also create DataFrames using randomly generated data. This is very useful when you want to practice analysis without needing a real dataset.

# import numpy as np
# import pandas as pd
# from numpy.random import randint

# np.random.seed(101)

# # Create a currency exchange rate table
# # 5 rows (Monday to Friday), 4 columns (currencies)
# data = pd.DataFrame(
#     randint(50, 800, (5, 4)),
#     index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
#     columns=['USDT', 'NGN', 'YEN', 'USD']
# )
# # print(data)




# # Accessing Data in a DataFrame
# # Once you have a DataFrame, you can look up specific columns or combinations of columns.

# # # Access a single column
# # data['USDT']          # returns the entire USDT column
# # type(data['USDT'])    # returns: <class 'pandas.core.series.Series'>
# # print(data['USDT'])

# # Access multiple columns
# data[['USDT', 'USD']]  # returns a new DataFrame with just the USDT and USD columns
# type(data[['USDT', 'USD']])  # returns: <class 'pandas.core.frame.DataFrame'>
# # print(data[['USDT', 'USD']])    


# # Adding and Dropping Columns
# # Adding a column
# # Add a Total column that sums all four currency columns
# data['Total'] = data['USD'] + data['USDT'] + data['NGN'] + data['YEN']




# # Dropping a column
# # Drop a single column permanently
# # data.drop('Gender', axis=1, inplace=True)

# # axis=1 means we are removing a column (not a row)
# # inplace=True means the change is applied directly to the DataFrame
# # Note: By default, axis is 0, which targets rows. Use axis=1 to target columns.



# # Filtering Data
# # You can filter a DataFrame to show only rows that meet certain conditions. This is similar to how you used boolean indexing in NumPy.

# # Show rows where USD column is greater than 0
# data[data['USD'] > 0]

# # Use AND to combine two conditions
# data[(data['USD'] > 0) & (data['YEN'] > 0)]

# # Use OR to combine two conditions
# data[(data['USD'] > 0) | (data['YEN'] > 0)]


# # You can also view general info about your DataFrame:
# data.info()     # shows data types, non-null counts, memory usage
# data.head()     # shows the first 5 rows
# data.tail()     # shows the last 5 rows



# # Handling Missing Data (NaN)
# # Real-world data almost always has missing values. Pandas gives you two main approaches for dealing with them:

# # Option 1: Drop rows with missing values
# data.dropna()

# # Option 2: Fill missing values
# # Fill all missing values with a fixed number
# data.fillna(value=20)

# # Fill missing values in a specific column with the column's mean
# data['sales'].fillna(value=data['sales'].mean())
# # Note: thresh by default is None. dropna() and fillna() are your two most common tools for dealing with NaN values.




# import numpy as np
# import pandas as pd

# scores = {
#     'Math':    [90, np.nan, 70],
#     'Science': [85, np.nan, np.nan],
#     'English': [95, 85, 75]
# }

# data = pd.DataFrame(scores, index=['Alice', 'Bob', 'Charlie'])
# print(data)


# # cleaned_data = data.dropna()
# # print(cleaned_data)

# data.dropna(inplace=True)
# print(data)


import pandas as pd

data = pd.read_csv('dataset/202002.csv')
print(data)


import pandas as pd

data = pd.read_excel('dataset/data.xlsx')
print(data)
