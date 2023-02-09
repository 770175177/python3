#!/usr/bin/python3

try:
	f = open('xxx.txt')
	#print(num)
	print("----1----")
except (NameError, FileNotFoundError):
	print("abnomal control")
#except FileNotFoundError:
#	print("file not found")
