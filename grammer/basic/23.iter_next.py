#!/usr/bin/python3

list = [1,2,3,4,5,6]
it = iter(list)		# create an iterator object
print(next(it))		# print the next item
print(next(it))		# print the next item

for x in it:
	print(x, end = ' ')

