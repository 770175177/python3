#!/usr/bin/python3

# 1.import 2.string 3.print

import tensorflow as tf 
import cv2
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
hello = tf.constant('hello tf')
sess = tf.Session()
print(sess.run(hello))
print('hello opencv')
