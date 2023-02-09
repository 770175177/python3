#!/usr/bin/python3

import numpy as np

A = np.array([[1,2],[1,1]]) 
B = np.array([[0,1],[2,2]])
print(A)
print("---------")
print(B)
print("---------")
print(A*B)
print("---------")
print(np.dot(A,B))

print(np.exp(2))
print(np.sqrt(B))

print("+++++++++++")
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.ravel())
a.shape = (6,2)
print(a)
print(a.T)
print(a.reshape(3,-1))
