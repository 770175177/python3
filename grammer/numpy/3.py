#!/usr/bin/python3

from numpy import pi
import numpy as np

a = np.arange(15).reshape(3,5)
print(a)

print(a.ndim)
print(a.size)
print(a.dtype.name)
print(a.dtype)

print(np.zeros((2,5)))
c = np.ones((2, 4), dtype = np.int32)
print(c)

e = np.linspace(0, 2*pi, 100)
print(e)

print(2**2)
