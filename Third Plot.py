import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 15, 100)
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 15, 30)
y2 = 4 + 1 * np.sin(2 * x2)

# plot
fig, ax = plt.subplots()

ax.plot(x2, y2 + 2.0, 'x', markeredgewidth=0.5)
ax.plot(x, y, linewidth=0.6)
ax.plot(x2, y2 - 2.0, '*', linewidth=0.5)

ax.set(xlim=(0, 10), xticks=np.arange(1, 11),
       ylim=(0, 10), yticks=np.arange(1, 11))

plt.show()
print("Plot has been shown!.Please watch")