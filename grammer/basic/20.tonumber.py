#!/usr/bin/python3

import math
import random

a = 1.0
b = 0

print(int(a))
print(float(b))
print(complex(a))
print(complex(a, b))
print('--------------')
a = -20
b = 5.5
c = [55, 555, 85, 53, 45]

print(abs(a))			# integer abs
print(math.fabs(a))		# float abs
print(math.ceil(b))		# to upper integer
print(math.floor(b))		# to lower integer
print(math.exp(2))		# e ^(x)
print(math.log(100, 10))	# log10(100)
print(math.log10(100))		# log10(100)
print(max(a, b))		# return max
print(min(a, b))		# return min
print(math.modf(b))		# depart integer and float
print(pow(b,2))			# b**2
print(round(b))			# 4 lose 5 save
print(math.sqrt(4))
print('--------------------')

print(random.choice(range(10))) # choise a num of 0-10
random.shuffle(c)
print(c)
print(random.uniform(10, 20))	# random create a float range 10-20
print(random.random())		# ceate a num range [0, 1)
print('+++++++++++++++++++')

print(math.sin(math.pi//2))
print(math.asin(1))
print(math.degrees(math.pi/2))
print(math.radians(58.7))
print(math.log(2,math.e))
