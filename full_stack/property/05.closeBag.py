#!/usr/bin/python3

def test(number):
	print('----1----')
	
	def test_in():
		print('----2----')
		print(number+100)

	print('----3----')
	return test_in

ret = test(100)
print('-'*50)
ret()
#test(100)()
