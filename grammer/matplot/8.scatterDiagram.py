#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#create data
x = np.arange(1,20, 2)
y = x
 
fig = plt.figure()	#create a chart
plt.scatter(x, y, c = 'r', marker = 'o')
#r represent red of the point,marker specify the shape as circle

plt.show()	#show all charts
