#!/usr/bin/python3

from multiprocessing import Pool
import time
import os

def test():
	print('---process in pool---pid=%d, ppid=%d'%(os.getpid(), os.getppid()))
	for i in range(3):
		print('---%d---'%i)
		time.sleep(1)
	return 'haha'

def test2(args):
	print('---callback func---pid=%d'%os.getpid())
	print('---callback func---args=%s'%args)

pool = Pool()
pool.apply_async(func=test, callback=test2)

#time.sleep(1)
while True:
	time.sleep(1)
	print('---main process---pid=%d'%os.getpid())

#pool.close()
#pool.join()
