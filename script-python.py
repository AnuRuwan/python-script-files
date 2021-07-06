import pandas as pn
import matplotlib.pyplot as plt
import numpy as np 
import sys

reg = pn.read_csv(sys.argv[1])
reg.plot.scatter(x = 'x', y = 'y', title = "Scatter plot-python")
plt.savefig('scatter-python.png')

xdata=reg['x']
ydata=reg['y']
plt.plot(xdata, ydata, 'o', color='blue')
m, b =np.polyfit(xdata, ydata, 1)
plt.plot(xdata,m*xdata+b)
plt.savefig('linearmodeling-py.png')
