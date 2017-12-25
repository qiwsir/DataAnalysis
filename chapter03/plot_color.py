#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np

NCURVES = 10
#np.random.seed(101)
curves = [np.random.random(20) for i in range(NCURVES)]
values = range(NCURVES)

fig = plt.figure()
ax = fig.add_subplot(111)
jet = cm = plt.get_cmap('jet') 
cnorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalar_map = cmx.ScalarMappable(norm=cnorm, cmap=jet)
#print scalarMap.get_clim()

lines = []
for idx in range(len(curves)):
    line = curves[idx]
    color_val = scalar_map.to_rgba(values[idx])
    color_text = ('color: (%4.2f,%4.2f,%4.2f)'%(color_val[0],color_val[1],color_val[2]))
    ret_line, = ax.plot(line, color=color_val, label=color_text)
    lines.append(ret_line)

handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

#ax.grid()

plt.show()

