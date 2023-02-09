#!/usr/bin/python3

from threading import Thread, Lock
from time import sleep
from queue import Queue

class Producer(Thread):
	def run(self):
		global queue
		count = 0
		while True:
			if queue.qsize() < 1000:
				for i in range(100):
					count += 1
					msg = 'produce '+str(count)
					queue.put(msg)
					print(msg)
				sleep(0.5)
class Consumer(Thread):
	def run(self):
		global queue
		while True:
			if queue.qsize() > 100:
				for i in range(3):
					msg = self.name+'consume '+queue.get()
					print(msg)
				sleep(1)

if __name__ == '__main__':
	queue = Queue()

	for i in range(500):
		queue.put('init products'+str(i))
	for i in range(2):
		p = Producer()
		p.start()
	for i in range(5):
		c = Consumer()
		c.start()
