#!/usr/bin/python3

# placehold

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
		     [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
		     [3, 4],
		     [5, 6]])
print(data4.shape)
with tf.Session() as sess:
	print(sess.run(data4))
	print(sess.run(data4[0]))	#row
	print(sess.run(data4[:, 0]))	#colomn
	print(sess.run(data4[0, 0]))
