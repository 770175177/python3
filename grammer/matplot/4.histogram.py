#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
 
plt.figure(1,dpi=100)	#create a chart
data = [1,1,1,2,2,2,3,3,4,5,5,4,4]

plt.hist(data)  #statistical incoming data

plt.show()	#show all charts
