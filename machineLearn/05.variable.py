#!/usr/bin/python3

# data type / count / procedure / dic / array

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#data1 = tf.constant(2.5)
data1 = tf.constant(2, dtype = tf.int32)
data2 = tf.Variable(10, name = 'var')
print(data1)
print(data2)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print(sess.run(data1))
print(sess.run(data2))
sess.close()
