#!/usr/bin/python3

import numpy as np

a = np.floor(10*np.random.random((2,2)))
b = np.floor(10*np.random.random((2,2)))
print(a)
print("--------")
print(b)
print("--------")
print(np.hstack((a,b)))
print("--------")
print(np.vstack((a, b)))
print("++++++++")
a = np.floor(10*np.random.random((2,12)))
print(a)
print("--------")
print(np.hsplit(a,3))
print(np.vsplit(a,2))
print("*********")
print(np.hsplit(a,(3,4)))
