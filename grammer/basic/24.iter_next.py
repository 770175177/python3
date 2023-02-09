#!/usr/bin/python3

import sys

list = [1,2,3,4,5,6]
it = iter(list)		# create iterator obj

while True:
	try:
		print(next(it))
	except StopIteration:
		sys.exit()
