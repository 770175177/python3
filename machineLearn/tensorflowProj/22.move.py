#!/usr/bin/python3
#1.API 2.count method 3.codes

import cv2
import numpy as np
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

matShift = np.float32([[1,0,100],[0,1,200]])
dst = cv2.warpAffine(img,matShift,(height,width))
cv2.imshow('dst', dst)
cv2.waitKey(0)
