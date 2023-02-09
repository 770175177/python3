#!/usr/bin/python3

import os
import time

g_num = 100

ret = os.fork()
if ret==0:
	print("----1----")
	g_num += 1
	print("----1---- g_num=%d"%g_num)

else:
	time.sleep(1)
	print("----2---- g_num=%d"%g_num)
	
