#!/usr/bin/python3
import numpy as np
import matplotlib.pylab as plt

x = np.linspace(-np.pi*2, np.pi*2, 100)
 #the x axis's domain of define 
plt.figure(1,dpi=50)	#create a chart

for i in range(1,5):
	plt.plot(x, np.sin(x/i))	#draw sin(x) function in ax2 subgraph

plt.show()	#show all charts
