#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([5,7,6,2,9,8,15,3])
plt.plot(x, y, 'r')	# curve (x, y, color)
plt.plot(x, y, 'g', lw = 10)	# curve (x, y, color,line wigth)
plt.show()
