#!/usr/bin/python3

from multiprocessing import Process
import time

class MyProcess(Process):
	def run(self):
		while True:
			print("----MyProcess----")
			time.sleep(1)

p = MyProcess()
p.start()

while True:
	print('----main----')
	time.sleep(1)
	
