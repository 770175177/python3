#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1,dpi=50)	#create a chart
ax1 = plt.subplot(211) 	#create subgraph ax1
ax2 = plt.subplot(212)	#create subgraph ax2

x = np.linspace(0, 10, 100) #the x axis's domain of define 

plt.sca(ax1) 	#select subgraph ax1
plt.plot(x, np.exp(x))	#draw exp(x) function in ax1 subgraph

plt.sca(ax2)	#select subgraph ax2
plt.plot(x, np.sin(x))	#draw sin(x) function in ax2 subgraph

plt.show()	#show all charts
