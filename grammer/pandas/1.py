#!/usr/bin/python3

import pandas as pds
pic_info = pds.read_csv("./data/mnist_10.csv")
print(type(pic_info))
#print(pic_info.dtypes)

print(pic_info.head(3))
print("---------------")
print(pic_info.tail(4))
print("---------------")
print(pic_info.columns)
print("---------------")
print(pic_info.shape)
print("---------------")
print(pic_info.loc[5])
print(pic_info.loc[5:6])
