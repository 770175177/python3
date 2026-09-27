#!/usr/bin/python3

#CURD

import numpy as np

data1 = np.array([1,2,3,4,5])
print(data1)
data2 = np.array([[1,2],[3,4]])
print(data2)
#shape
print(data1.shape, data2.shape)
#zero ones
print(np.zeros([2,3]), np.ones([2,3]))
#modify search
data2[1,0] = 5
print(data2) 
print(data2[1,1])
#num count
data3 = np.ones([2,3])
print(data3*2)
print(data3/3)
print(data3+2)
#matrx +
data4 = np.array([[1,2,3],[4,5,6]])
print(data3 + data4)
print(data3 * data4)
