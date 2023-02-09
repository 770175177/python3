#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1,dpi=50)	#create a chart
x = np.linspace(-np.pi,np.pi,800)
#x axis areas from -3.14 to 3.14, and spaced 100 pixels apart
plt.plot(x,np.sin(x))
plt.show()	#show all charts
