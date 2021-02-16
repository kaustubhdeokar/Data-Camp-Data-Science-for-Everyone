import pandas as pd

dogs = pd.read_csv('dogs.csv')
#print(dogs.columns)

#print(dogs.index)

# We can move a column from the body of the dataframe to the index.

df = pd.DataFrame(dogs)
#print("DataFrame:")
#print(df)

dog_index = df.set_index("name")
#print(dog_index)

#To undo setting the index as a column

reset_df = dog_index.reset_index()

#To remove the column completely which was set as index.

drop_name_column = dog_index.reset_index(drop=True)

#Why should we do subsetting ???
'''
1.  To print rows with a particular name we would have to do.
    df[df["name"].isin(["option1","option2"])]

    Now as indexes contains the name we can do

    df.loc[["option1","option2']]

2.  Indexes can have duplicate entries

3.  We can have multiple columns as indexes.
    
'''

multiple_columns_as_index = df.set_index(["breed","name"])
print(multiple_columns_as_index)

subsetting_by_multiple_cols_as_index = multiple_columns_as_index.loc[[("labrador","bella"),("poodle","charlie")]]
print(subsetting_by_multiple_cols_as_index)

'''
Sort

df.sort_index()

df.sort_index(level=["col1","col2"],ascending=[True,False])

'''
