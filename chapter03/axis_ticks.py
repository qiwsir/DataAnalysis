#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 5.0, 0.02)
y = np.exp(-x)*np.cos(2*np.pi*x)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8,0.8])
ax.plot(x, y)

ax.grid(color='gray')
ax.set_xlabel("x")
ax.set_xticks(np.linspace(0, 5, 6),('zero', 'one', 'two', 'three', 'four', 'five'))


plt.show()
