import matplotlib.pyplot as plt
import numpy as np

year_x =[1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959]

pop_y =[2.53, 2.57, 2.62, 2.67, 2.71, 2.76, 2.81, 2.86, 2.92, 2.97]

bubble_sizes = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927,20.434176, 8.199783, 0.708573, 150.448339, 10.392226]

np_bubble_sizes = np.array(bubble_sizes)*3

plt.scatter(year_x,pop_y,s=np_bubble_sizes,alpha=0.8)

plt.xscale('log')

plt.grid(True)
plt.show()

