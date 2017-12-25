#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

t = np.linspace(0, 100, 100)
s = 9.8 * np.power(t, 2) / 2
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, s)

ax.set_ylabel('displacement')
ax.set_xlim(0, 100)
ax.set_xlabel('time')

xmajor_locator   = MultipleLocator(20)
xmajor_formatter = FormatStrFormatter('%1.1f')
xminor_locator   = MultipleLocator(5)

ymajor_locator   = MultipleLocator(10000)
ymajor_formatter = FormatStrFormatter('%1.1f')  
yminor_locator   = MultipleLocator(5000) 

ax.xaxis.set_major_locator(xmajor_locator)
ax.xaxis.set_major_formatter(xmajor_formatter)

ax.yaxis.set_major_locator(ymajor_locator)  
ax.yaxis.set_major_formatter(ymajor_formatter) 

ax.xaxis.set_minor_locator(xminor_locator)  
ax.yaxis.set_minor_locator(yminor_locator) 

ax.grid(True, which='major')
ax.grid(True, which='minor')

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)

plt.show()
