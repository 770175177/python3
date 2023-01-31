#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as msc

print("input which pic you want to test?")
#print("like pic2")
#pic_path = input("like pic2.png : ")
pic_path = "num_pic/" + "pic2.png"
#print(pic_path)

img_array = msc.imread(pic_path, flatten = True)
img_data = 255.0 - img_array.reshape(784)
#img_data = (img_data / 255.0 * 0.99) + 0.01
#print(img_data)
#print(img_array)
np.savetxt("mnist_dataset/pic_pix.txt", img_data,  fmt = '%f', delimiter = ",")

img_data = np.loadtxt("mnist_dataset/pic_pix.txt", delimiter = ',')
print(img_data)


