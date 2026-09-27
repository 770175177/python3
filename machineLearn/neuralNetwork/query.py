#!/usr/bin/python3

import scipy.misc as msc
import numpy as np
import scipy.special as spc
import matplotlib.pyplot as plt
#self.activation_function = lambda x: scipy.special.expit(x) 		
		
def query(inputs_list, weight_ih, weight_ho) :
	inputs = np.array(inputs_list, ndmin = 2).T		

	hidden_inputs = np.dot(weight_ih, inputs)
	hidden_outputs = spc.expit(hidden_inputs)

	final_inputs = np.dot(weight_ho, hidden_outputs)
	final_outputs  = spc.expit(final_inputs)

	return final_outputs
	pass

wih = np.loadtxt("mnist_dataset/wih.txt",  delimiter = ',')
who = np.loadtxt("mnist_dataset/who.txt",  delimiter = ',')

for i in range(20) :
	print("which pic you want to test?")
	pic_num = input("a pic num : ")
	#pic_num = '%d'%pic_num
	pic_path = "num_pic/pic" + pic_num + ".png"
	#pic_path = "num_pic/pic2.png"

	img_array = msc.imread(pic_path, flatten = True)
	img_data = 255.0 - img_array.reshape(784)
	inputs = (img_data / 255.0 * 0.99) + 0.01

	outputs = query(inputs ,wih ,who)
	corrent = np.argmax(outputs)

	print("the num of the pic is : ", corrent)
	corrent = '%d'%corrent
	pic_path = "num_pic/pic" + corrent + ".png"
	img_array = msc.imread(pic_path, flatten = True)
	plt.imshow(img_array, cmap='Greys', interpolation = 'None')
	plt.show()

