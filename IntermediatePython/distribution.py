import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
final_tails=[]
for x in range(100):
    tails=[0]
    for i in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[i]+coin)
    final_tails.append(tails[-1])

plt.hist(final_tails,bins=10)
plt.show()
