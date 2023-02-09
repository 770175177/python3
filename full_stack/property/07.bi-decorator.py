#!/usr/bin/python3

def w1(func):
	print('----decorating1---')
	def inner():
		print('----poving1----')
		func()
	return inner

def w2(func):
	print('----decorating2---')
	def inner():
		print('----poving2----')
		func()
	return inner

@w1
@w2
def f1():
	print("---f1---")

f1()
