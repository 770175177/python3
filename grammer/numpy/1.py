#!/usr/bin/python3

import numpy as np

wd = np.genfromtxt("./data/1.txt", delimiter = ',', dtype = str)
print(type(wd))
print(wd)
#print(help(np.genfromtxt))

vector = np.array([45,55,65])
matrix = np.array([[78,45,55],[45,48,65],[12,42,33]])

print(vector)
print(matrix)

print(vector.shape)
print(matrix.shape)

number = np.array([1,2,3,4.0])
print(number.dtype)
print(number)

print(vector == 55)

