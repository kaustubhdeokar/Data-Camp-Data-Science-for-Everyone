import pandas as pd
dogs = pd.read_csv('dogs.csv')
df = pd.DataFrame(dogs)

df_named_index = df.set_index("name")
#print(df_named_index)

#Slicing
'''
Before slicing important to sort.
Last index is included
Works only for outer index level
'''
df_sorted = df_named_index.sort_index()

df_sliced = df_sorted.loc[:"lucy"]

#print(df_sliced)

'''
Correct approach for slicing inner index levels is to pass tuples
(First and last index)
'''

df_named_breed_index = df.set_index(["name","breed"])
#print(df_named_breed_index)

df_sorted_indexes = df_named_breed_index.sort_index()
#print(df_sorted_indexes)

df_sliced_2 = df_sorted_indexes.loc[("bella","labrador"):("stella","chihuahua")]
#print(df_sliced_2)

'''
Slicing columns
'''
df_columns = df.loc[:,"name":"color"]
print(df_columns)


'''
Slicing columns by ILOC
'''
df_iloc_subsetting = df.iloc[1:3,2:4]
print(df_iloc_subsetting)
