#!/usr/bin/python3

import numpy as np

matrix = np.array([[78,45,55],[45,48,65],[12,42,33]])

print(matrix)
print(matrix.shape)

print(matrix[:,1])
print(matrix[:,0:2])

index = (matrix == 48)

print(matrix.dtype)
matrix = matrix.astype(float)
print(matrix)
print(matrix.dtype)
print(matrix.min())
print(matrix.max())

print(matrix.sum(axis=1))
print(matrix.sum(axis=0))
