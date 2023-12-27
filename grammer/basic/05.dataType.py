#!/usr/bin/python3

''' 
 there are 6 types of data
 Number/ String/ List/ Tuple/ Set/ Dictionary
 immutable data: Number/ String/ Tuple
 variable data:  List/ Dictionary/ Set
'''

# number: int/ float/ bool/ complex
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

# type not thinks sub class is a father class
# isinstance thinks sub class is a father class
print("a(%d)'s type is int?"% a, isinstance(a, int))

# change number type from float to int
print(int(b))

# change number type from int to float
print(float(a))

# change to string
print(str('3.0'))

print('number type: int/bool/float/complex')
# int num 
num = 1

# bool bool_type 
bool_type = True

# float a/b
a = 1.23
b = 3E-2

# complex com 
com = 1 + 5j

print(num)
print(bool_type)
print(a)
print(b)
print(com)

print("string")
var1 = "hello world"
var2 = 'heng'
print("var1[0]: ", var1[0])
print("var2[1:4]: ", var2[1:4])
print("update: ", var1[:6] + "heng")

print("list")
li1 = ['google', 'baidu', 1990, 200]
print(li1[0])
print(li1[-1])
li1.append('taobao')
print(li1)
del li1[1]
print(li1)

print("tuple")
tup=(1,2,34,3)
print(tup)
print(max(tup))
print(min(tup))

print('directory')
d = {'k1': 422, 'k2': 533, 'web': 'www.baidu.com'}
print(d)
print('d[k2]', d['k2'])
print(d.keys())

print("set")
set1 = {2, 3, 4, 5, 23}
set2 = set([4, 5, 7, 9])
print(set2)
set1.add(67)
print(set1)
set1.update((22, 89))
print(set1)
set1.update({6, 10})
print(set1)
set1.update({0, 1}, [33, 45])
print(set1)
set1.remove(10)
print(set1)
