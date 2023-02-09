#!/usr/bin/python3

import time
from threading import Thread

g_num = 0

class test1():
	global g_num
	for i in range(1000000):
		g_num += 1

	print("---test1--g_num=%d---"%g_num)

class test2():
	global g_num
	for i in range(1000000):
		g_num += 1

	print("---test2--g_num=%d---"%g_num)

p1 = Thread(target=test1)
p1.start()
#time.sleep(1)

p2 = Thread(target=test2)
p2.start()

print('---g_num=%d---'%g_num)
