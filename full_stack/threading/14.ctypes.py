#!/usr/bin/python3

from ctypes import *
from threading import Thread

#load dll
lib = cdll.LoadLibrary('./libdeadloop.so')

#create son a process, candle c func
t = Thread(target=lib.DeadLoop) 
t.start()

while True:
	pass
