import pandas as pd

data = pd.read_csv('environment_data.csv')

df = pd.DataFrame(data)

#Sorting by Element Code column.

sorted_df = df.sort_values("Element Code")

# reverse

reverse_sort = df.sort_values("Element Code",ascending=False)

#sort by multiple columns

multiple_col_sort = df.sort_values(["Area Code","Element Code"])

#sort multiple columns, multiple variations.

multiple_col_sort_2 = df.sort_values(["Area Code","Element Code"],ascending=[True,False])


#Subsetting.

#Filtering Rows

rows_element_code_above_7000 = df[df["Element Code"]>7000]

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)
