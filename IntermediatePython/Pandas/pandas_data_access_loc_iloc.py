import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

dic = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

df = pd.DataFrame(dic)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

df.index = row_labels

print(df.loc["JPN"]) #as series

print(df.loc[["AUS","IN"]]) #as dataframe

print(df.loc["US","cars_per_cap"]) # value

print(df.iloc[2])

print(df.iloc[[1,3]])

print(df.iloc[1,2])
