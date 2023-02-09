#!/usr/bin/python3

# 1.import opencv 2.API 3.stop

import cv2

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
(b, g, r) = img[100,100]
print(b,g,r)

# 10 100 --- 110 100
for i in range(1, 100):
	img[10 + i, 100] = (255, 0 ,0)
cv2.imshow('image', img)
cv2.waitKey(0) 			#1000  =  1000ms

