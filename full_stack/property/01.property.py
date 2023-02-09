#!/usr/bin/python3

class Test(object):
	def __init__(self):
		self.__num = 100
	
	def getNum(self):
		return self.__num

	def setNum(self, newNum):
		self.__num = newNum


	num = property(getNum, setNum)

t = Test()
print(t.getNum())
t.setNum(50)
print(t.getNum())
print("*"*50)
t.num = 200
print(t.num)
