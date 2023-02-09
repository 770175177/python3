#!/usr/bin/python3

# 1.import opencv 2.API 3.stop

import cv2
#import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

img = cv2.imread('./file/01.jpg', 1)	# 0 gray,  1 color
cv2.imwrite('./file/02.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 10])	# img name, img data, img quality 0-100(lose some quality)
cv2.imwrite('./file/02.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])	#img name, img data, img quality 0-9(not lose quality)

