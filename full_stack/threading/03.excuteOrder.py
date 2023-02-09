#!/usr/bin/python3

import time
import threading

class MyThread(threading.Thread):
	def run(self):
		for i in range(3):
			print("---Thread class-name=%s-@-%d---"%(self.name, i))
			time.sleep(1)

def test():
	for i in range(5):
		t = MyThread()
		t.start()

if __name__ == '__main__':
	test()
