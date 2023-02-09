#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt
%matplotlib inline

a = numpy.zeros([3,2])
print(a)
print(" ")
a[0,0] = 1
a[0,1] = 2
a[1,0] = 9
a[2,1] = 12

plt.imshow(a,interpolation="nearest")
ply.show()
