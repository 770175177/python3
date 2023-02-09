#!/usr/bin/python3

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

mat0 = tf.constant([[0,0,0], [0,0,0]])
mat1 = tf.zeros([2, 3])
mat2 = tf.ones([3, 2])
mat3 = tf.fill([2, 3], 15)
with tf.Session() as sess:
	#print(sess.run(mat0))
	print(sess.run(mat1))
	print(sess.run(mat2))
	print(sess.run(mat3))
