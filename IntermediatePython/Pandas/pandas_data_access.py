import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

dic = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

dataFrame = pd.DataFrame(dic)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

dataFrame.index = row_labels

print(dataFrame)

###############################

# 1. Printing only a single column


