#!/usr/bin/python3

import os

ret = os.fork()
if ret==0:
	print("son, pid=%d, ppid=%d"%(os.getpid
(), os.getppid()))
else:
	print("father, pid=%d, ret=%d"%(os.getpid(), ret))
	
