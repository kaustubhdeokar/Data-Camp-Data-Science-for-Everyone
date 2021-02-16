import pandas as pd

data = pd.read_csv('netflix_titles.csv')

df = pd.DataFrame(data)

#drop duplicates in a column.

countries = df.drop_duplicates(subset="director")

#count values

directors = countries["director"].value_counts()

print(directors)
