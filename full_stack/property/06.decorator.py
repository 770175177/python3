#!/usr/bin/python3

def w1(func):
	def test_in():
		print('----poving----')
		func()
	return test_in

@w1
def f1():
	print("---f1---")

def f2():
	print('---f2---')

f1()
