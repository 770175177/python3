#!/usr/bin/python3

from multiprocessing import Process
import time

def test():
	for i in range(5):
		print("----test----")
		time.sleep(1)

p = Process(target=test)
p.start()
p.join()

while True:
	print('----main----')
	time.sleep(1)
	
