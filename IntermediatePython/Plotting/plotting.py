import matplotlib.pyplot as plt

year_x =[1950, 1960, 1970, 1980, 1990]

pop_y =[2.53, 2.57, 2.62, 2.67, 2.71]

plt.plot(year_x,pop_y)

plt.xlabel('year')
plt.ylabel('population')
plt.title('world population projection')

plt.show()

