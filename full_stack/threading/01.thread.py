#!/usr/bin/python3

import time
from threading import Thread

def test():
	print("---drink a little---")
	time.sleep(1)

for i in range(5):
	t = Thread(target=test)
	t.start()
