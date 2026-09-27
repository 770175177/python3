#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([5,7,6,2,9,8,15,3])
plt.bar(x, y, 0.5, alpha = 1,color = 'b')	#histogram  (x, y, each hist ratio, tranparent, color)
plt.show()
