import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

dic = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

df = pd.DataFrame(dic)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

df.index = row_labels

print(df)

print('------------------------------------COLUMN ACCESS----------------')

# 1. Printing only a single column


print(df["drives_right"])

print(type(df["drives_right"])) #Series

#to make a dataframe out of a column

print(df[["drives_right"]])

#multiple columns
df[["country","drives_right"]]
