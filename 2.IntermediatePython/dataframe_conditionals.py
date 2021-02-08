import pandas as pd
import os
import numpy as np

data = pd.read_csv('./brics.csv',index_col=0)

#conditionals with dataframe
print('data with area>7')
print(data[data["area"]>7])

#with and,or etc..`
print('data with population over 100 or area>7')
print(data[np.logical_or(data["area"]>7,data["population"]>100)])

print('data with population over 100 and area>7')
print(data[np.logical_and(data["area"]>7,data["population"]>100)])
