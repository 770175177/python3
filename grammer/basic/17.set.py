#!/usr/bin/python3

student = {'Tomy', 'Jimy', 'Mary', 'Jack', 'Rose'}

print(student)
if 'Tom' in student:
	print('Tom in set')
elif 'Jim' in student:
	print('Jim in set')
else:
	print('Jim and Tom are not in set')

print('-------------')
a = set('asadcsdcsd')
b = set('alacas')

print(a)
print(a - b)		# a and b are both have
print(a | b)		# a or b are both have
print(a & b)		# intersection
print(a ^ b)		# neither a or b has
