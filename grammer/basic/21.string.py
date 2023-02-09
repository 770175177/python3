#!/usr/bin/python3

str1 = 'hello world'
str2 = 'robut'
lis = ['hekl', 'google','baidu']

print('str1[0]:', str1[0])
print('str2[1:4]', str2[1:4])

print('my name is %s, %d years old ' %('XiaoMing', 10))

print(str1.capitalize())	# the first alph to upper
print(str2.center(32, ))
print(str1.count('e'))
#print(bytes.decode(encoding = 'utf-8', errors = 'ignore'))
del lis[2]
print(lis)
print(len(lis))
print(len(str1))
for x in str1:
	print(x)
	pass
print(max(lis))
