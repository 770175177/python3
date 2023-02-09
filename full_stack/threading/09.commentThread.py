#!/usr/bin/python3

import  threading 
import time

def test1():
	name = threading.current_thread().name
	print('----thread name is %s----'%name)
	num = 100
	if name == 'Thread-1':
		num+=1
	else:
		time.sleep(1)
	print("---thread is %s--num=%d---"%(name, num))

p1 = threading.Thread(target=test1)
p1.start()

p2 = threading.Thread(target=test1)
p2.start()

