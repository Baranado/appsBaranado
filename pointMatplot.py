import os
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [4]
y = [3]
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid()
plt.plot(x, y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
#plt.show()
plt.savefig("matplotlib.png")
os.system("termux-open matplotlib.png")
