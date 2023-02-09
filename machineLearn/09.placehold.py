#!/usr/bin/python3

# placehold

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

data1 = tf.placeholder(tf.float32)
data2 = tf.placeholder(tf.float32)
dataAdd = tf.add(data1, data2)
with tf.Session() as sess:
	print(sess.run(dataAdd, feed_dict = {data1: 6, data2: 2}))
print('end!')
