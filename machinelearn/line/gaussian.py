import matplotlib.pyplot as plt
import numpy as np
import math
def gaussian(sigma, x, u):
	y = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
	return y
#x = np.linspace(220, 230, 10000)
x = np.linspace(-8, 8, 10000)

plt.title('PDF in Horizontal Direction', fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
axes = plt.subplot(111)
#axes.set_xticks([-800,-400,0,400,800])
#axes.set_yticks([0,0.001,0.002,0.0030])
plt.plot(x, gaussian(1, x, 0), "b-", linewidth=1)
plt.show()

##高斯分布