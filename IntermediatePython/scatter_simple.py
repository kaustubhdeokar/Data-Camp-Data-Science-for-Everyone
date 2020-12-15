import matplotlib.pyplot as plt
gdp=[974.5803384,
 5937.029525999998,
 6223.367465,
 4797.231267,
 12779.37964,
 34435.367439999995,
 36126.4927,
 29796.04834,
 1391.253792,
 33692.60508]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441]

plt.scatter(gdp_cap, life_exp)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val,tick_lab) # plt.yticks([..],[labels for ..]) y axis should be ..
