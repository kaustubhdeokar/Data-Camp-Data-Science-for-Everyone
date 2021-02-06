import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

dic = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

df = pd.DataFrame(dic)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

df.index = row_labels


print('limited functionality,cannot slice rows and columns together')

#Row Access loc.
print('-----------------------------------------LOC-----------------------------------------')

print(df.loc["US"]) #type series

print(df.loc[["US","IN","JPN"]])

#row and column access

print(df.loc[["US","IN"],["country","drives_right"]])

#print all rows and selected columns

print(df.loc[:,["country","drives_right"]])
#all column selected rows
print(df.loc[["IN"],:])


#ILOC
print('-----------------------------------------ILOC-----------------------------------------')
print(df.iloc[:,[0,1]])
print(df.iloc[[1,2,3],[1,2]])
