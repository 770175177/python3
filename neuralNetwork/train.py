#!/usr/bin/python3

import scipy.misc as msc
import numpy as np
import scipy.special
import matplotlib.pyplot as plt

class neuralNetwork :
	
	def __init__(self , inputnodes , hiddennodes , outputnodes , learninggrate) :
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes

		self.lr = learninggrate
		
		#self.wih = (np.random.rand(self.hnodes, self.inodes) - 0.5)
		#self.who = (np.random.rand(self.onodes, self.hnodes) - 0.5)
		self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
		self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
		
		self.activation_function = lambda x: scipy.special.expit(x) 		
		pass

	def train(self, inputs_list, targets_list) :
		inputs = np.array(inputs_list, ndmin = 2).T
		targets = np.array(targets_list, ndmin = 2).T

		hidden_inputs = np.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = np.dot(self.who, hidden_outputs)
		final_outputs = self.activation_function(final_inputs)
		
		output_errors = targets - final_outputs
		hidden_errors = np.dot(self.who.T, output_errors)

		self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))

		self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
		pass

	def query(self, inputs_list) :
		inputs = np.array(inputs_list, ndmin = 2).T		

		hidden_inputs = np.dot(self.wih, inputs)
		hidden_outputs = self.activation_function(hidden_inputs)

		final_inputs = np.dot(self.who, hidden_outputs)
		final_outputs  = self.activation_function(final_inputs)

		return final_outputs
		pass

input_nodes = 784
hidden_nodes = 200
output_nodes = 10

learning_rate = 0.1

n = neuralNetwork(input_nodes , hidden_nodes , output_nodes , learning_rate)

#print(n.wih)
#print(n.who)
#n.query([1.0, 0.5, -1.5])

training_data_file = open("./mnist_dataset/mnist_train.csv" , 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()
#print(len(data_list))
#print(data_list[0])

epochs = 5

for e in range(epochs) :
	for record in training_data_list :
		all_values = record.split(',')
		#image_array = np.asfarray(all_values[1:]).reshape((28,28))
		#plt.imshow(image_array, cmap='Greys', interpolation = 'None')
		#print(image_array)
		#plt.show()
		inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
		targets = np.zeros(output_nodes) + 0.01
		targets[int(all_values[0])] = 0.99
		#print(targets)
		n.train(inputs, targets)
		#print(targets)
		pass
	pass

np.savetxt("mnist_dataset/wih.txt", n.wih, fmt = '%f', delimiter = ',')
np.savetxt("mnist_dataset/who.txt", n.who, fmt = '%f', delimiter = ',')

#print("which pic you want to test?")
#pic_path = input("like pic0.png : ")
#pic_path = "num_pic/" + pic_path

#img_array = msc.imread(pic_path, flatten = True)
#img_data = 255.0 - img_array.reshape(784)
#inputs = (img_data / 255.0 * 0.99) + 0.01
#outputs = n.query(inputs)
#corrent = np.argmax(outputs)

#print("the num of the pic is : ", corrent)


test_data_file = open("mnist_dataset/mnist_test.csv",'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[0].split(',')
#print(all_values[0])

#image_array = np.asfarray(all_values[1:]).reshape((28, 28))
#plt.imshow(image_array, cmap='Greys', interpolation = 'None')
#plt.show()

#print(n.query((np.asfarray(all_values[1:]) / 255.0 *0.99) + 0.01))

scorecard = []

for record in test_data_list :
	all_values = record.split(',')
	corrent_label = int(all_values[0])
	#print(corrent_label, "corrent lable")
	inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) +0.01
	outputs = n.query(inputs)
	label = np.argmax(outputs)
	#print(label, "network's answer")
	if (label == corrent_label) :
		scorecard.append(1)
	else :
		scorecard.append(0)
	pass
	pass
#print(scorecard)

scorecard_array = np.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size)


