#!/usr/bin/python3

import cv2
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
# [100,200] x
# [100,300] y
img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
imgInfo = img.shape
dst = img[100:200,100:300]
cv2.imshow('image', dst)
cv2.waitKey(0)
