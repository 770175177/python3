#!/usr/bin/python3

from threading import Thread, Lock
import time

def test1():
	num = 100
	num+=1
	print("---test1- num=%d--"%num)
	time.sleep(2)
	print("---test1- num=%d--"%num)

def test2():
	time.sleep(1)
	num=100
	print("---test2- num=%d--"%num)

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test2)
p2.start()

