#!/usr/bin/python3

# 1.load 2.info 3.resize 4.check

import cv2
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
# 1.enlarge, reduce 2.equal proportion, non equal proportion
''' method
1.Nearest domain interpolation
2.bilinear interpolation
3.Pixel relation resampling
4.cubic interpolation
'''
'''
2.bilinear interpolation
(15,22) |  |	|(15,23)
------------------------
     ---|--|----|---
	|  |(15.22,22.3)
	|  |	|
------------------------
(16,22) |  |	|(16,23)
'''
# A1 = 20% up + 80% down	A2
# B1 = 30% left + 70% right 	B2
# dst1 = A1 30% + A2 70% 
# dst2 = B1 20% + B2 80%
#method2_bilinear interpolation  
distHeight = int(height*0.5)
distWidth = int(width*0.5)
dst = cv2.resize(img, (distWidth, distHeight))
cv2.imshow('image', dst)		# windows name, img
cv2.waitKey(0)


