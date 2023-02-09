#!/usr/bin/python3

import pandas as pds
pic_info = pds.read_csv("./data/mnist_10.csv")
print(pic_info["7"])
