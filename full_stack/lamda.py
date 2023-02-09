#!/usr/bin/python3

def test(a,b,func):
	return func(a,b)
#print(test(11,55,lambda x,y:x+y))

fun_new = input("input a fun:")
fun_new = eval(fun_new)
print(test(12,45,fun_new))
