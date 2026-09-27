#!/usr/bin/python3

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

mat1 = tf.constant([[2],[3],[4]])
mat2 = tf.zeros_like(mat1)
mat3 = tf.linspace(0.0, 2.0, 11)
mat4 = tf.random_uniform([2,3], -1, 2)
with tf.Session() as sess:
	print(sess.run(mat1))
	print(sess.run(mat2))
	print(sess.run(mat3))
	print(sess.run(mat4))

