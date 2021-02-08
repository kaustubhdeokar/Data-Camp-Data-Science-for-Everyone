import pandas as pd

data = pd.read_csv('environment_data.csv')

print(data.head())


print(data.shape)

df = pd.DataFrame(data)
print(df.describe)

#.info() shows information on each of the columns, such as the data type and number of missing values.

info = df.info()
print('info = {}'.format(df))

#all the values of a dataframe in a 2-d numpy array.
values = df.values

columns = df.columns

#adding new column
df["Element Code 2"] = df["Element Code"]+10
