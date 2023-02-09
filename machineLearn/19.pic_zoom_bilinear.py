#!/usr/bin/python3

# 1.load 2.info 3.resize 4.check

import cv2
import numpy as np
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]

# 1.enlarge, reduce 2.equal proportion, non equal proportion
''' method
1.Nearest domain interpolation
2.bilinear interpolation
3.Pixel relation resampling
4.cubic interpolation
'''
'''
1.nearest domain interpolation

src 10*20 -> dst 5*10
dst <- src
(1,2) <- (2,4)
dst x 1 -> src x 2 newX
newX = x*(src row / dst row) 	   newX = 1*(10/5) = 2
newY = y*(src colomn / dst colomn) newY = 2*(20/10) = 4
12.3 = 12
'''
#method2_bilinear interpolation  
dstHeight = int(height/2)
dstWidth = int(width/2)
dstImage = np.zeros((dstHeight, dstWidth,3), np.uint8) # 0-255
for i in range(0, dstHeight): #row
	for j in range(0, dstWidth): #colomn
		iNew = int(i * (height*1.0/dstHeight))
		jNew = int(j * (width*1.0/dstWidth))
		dstImage[i,j] = img[iNew,jNew]
cv2.imshow('image', dstImage)		# windows name, img
cv2.waitKey(0)


