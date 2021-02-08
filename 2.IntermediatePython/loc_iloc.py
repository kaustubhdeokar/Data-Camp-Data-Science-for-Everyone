import pandas as pd

brics = pd.read_csv('./brics.csv',index_col=0)

print('select a particular country column:- data[columnname]')
print(brics["country"])
print('type of the above is object')

print('select a particular country column as a dataframe:- data[[columnname]]')
print(brics[["country"]])
print('type of the above is dataframe')

print('select multiple columns')
print(brics[["country","capital"]])


print('\n\nselect a particular row use slicing as data[_:_]')
print(brics[1:4])

print('row with loc')
print(brics.loc["IN"])
print('multiple rows with loc-only with dataframes')
print(brics.loc[["IN","RU"]])

print('multiple rows with multiple column also')
print(brics.loc[["IN","RU"],["capital","population"]])

print('multiple rows with all columns also')
print(brics.loc[["IN","RU"],:])

print('similarly with the iloc')
print(brics.iloc[[1,2,3],[1,2,3]])

print(brics.iloc[:,[1,2]])
