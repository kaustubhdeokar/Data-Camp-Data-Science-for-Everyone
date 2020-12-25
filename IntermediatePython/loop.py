from random import randint
import numpy as np
import pandas as pd

dict={}
for i in range(97,97+10):
    dict[chr(i)]=i-96

for key,value in dict.items():
    print(str(key)+" corresponds to "+str(value))

height=[randint(0,100) for i in range(10)]
weight=[randint(0,100) for i in range(10)]

np_height = np.array(height)
np_weight = np.array(weight)

combined = np.array([np_height,np_weight])
print(combined)

print('for looping over multi dimensional numpy array use nditer')

for var in np.nditer(combined):
    print(var)

def uppercase(str):
    return str.upper()


print('\n\n this is a dataframe')
brics = pd.read_csv('./brics.csv',index_col=0)
print(brics)
print('\n\n to iterate over this dataframe use iterrows()')
print('here we add a column based on criteria with area>10')
for label,data in brics.iterrows():
    brics.loc[label,"countrysize"]=brics.loc[label]["area"]>float(10)
print(brics)

print('A more efficient way being')
brics["length"]=brics["country"].apply(uppercase)
print(brics)

