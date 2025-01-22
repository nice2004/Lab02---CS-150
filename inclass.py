import pandas as pd

# Creating and printing a series
series = pd.Series([42, 21, 7, 3.5])
print(series)

# Creating and printing a dataframe
data_frame = pd.DataFrame({'age': 18,
                           'name': ['Alice', 'Bob', 'Carl'],
                           'cardio': [60, 70, 80]})
print(data_frame)

# Selecting elements in dataframes

# Selecting by Column
print(data_frame['age'])
print(data_frame['name'])

#  Select by index and slice
print(data_frame[2:3])
print(data_frame.iloc[2, 1])

# Boolean Indexing
print(data_frame[data_frame['cardio'] > 60])

# Select by Label
print(data_frame.loc[:, 'name'])
print(data_frame.loc[:, ['age', 'cardio']])

# Modifying an existing dataframe

data_frame['age'] = 16
print(data_frame)

data_frame.loc[1:, 'age'] = 16
print(data_frame)

data_frame.loc[:, 'friend'] = 'Nice'
print(data_frame)

# the same can be accomplished with a simpler code
data_frame['friend'] = 'Alice'
print(data_frame)

