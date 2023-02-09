#!/usr/bin/python3

# there are 6 types of data
# Number/ String/ List/ Tuple/ Set/ Dictionary
# immutable data: Number/ String/ Tuple
# variable data:  List/ Dictionary/ Set

#number: int/ float/ bool/ complex
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))
print('-----------------')
print(isinstance(a, int))
print('-----------------')
class A:
	pass

class B(A):
	pass
print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)
