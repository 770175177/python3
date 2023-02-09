#!/usr/bin/python3

import os
import time

ret = os.fork()
if ret==0:
	while True:
		print("son")
		time.sleep(1)
else:
	while True:
		print("father, id=%d"%ret)
		time.sleep(1)
	
