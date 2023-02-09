#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt', delimiter=',')
print(data)
plt.plot(data[:,0],data[:,1], 'or')

plt.show()	#show all charts
