#!/usr/bin/python3

import numpy as np

a = np.arange(12)
b = a
c = a.view()
d = a.copy()
print(a)
print(a is b)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
a[5] = 0
print(b) 
print("-------")
print(a is c)
print(c.shape)
print(c)
print("------")
print(d)
