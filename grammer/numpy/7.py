#!/usr/bin/python3

import numpy as np

data = np.sin(np.arange(20)).reshape(5,4)
print(data)
idx = data.argmax(axis = 0)
print(idx)
print("--------")
print(data[idx,range(data.shape[1])])
print("--------")
print(range(data.shape[1]))
print("++++++++")
a = np.arange(0,40,10)
print(a)
b = np.tile(a, (3,5))
print(b)

print(">>>>>>>>>>")
a = np.array([[4,3,5],[1,2,1]])
print(a)
print("---------")
print(np.sort(a, axis = 1))
print(np.argsort(a))
