import matplotlib.pyplot as plt
import numpy as np
gdp_cap=[974.5803384, 5937.029525999998,6223.367465, 4797.231267, 12779.37964, 34435.367439999995,
 36126.4927, 29796.04834, 1391.253792, 33692.60508]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441]
pop=[31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226]
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)
# Double np_pop
np_pop*=4

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
