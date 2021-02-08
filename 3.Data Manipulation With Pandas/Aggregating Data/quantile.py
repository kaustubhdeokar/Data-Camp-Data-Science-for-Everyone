import pandas as pd

def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

data = pd.read_csv('./quantile.csv')
print(data["Col"].agg(iqr))


