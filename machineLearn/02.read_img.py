#!/usr/bin/python3

# 1.import opencv 2.API 3.stop

import cv2
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
cv2.imshow('image', img)		# windows name, img
cv2.waitKey(0)


