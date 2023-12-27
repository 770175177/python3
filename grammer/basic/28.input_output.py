#!/usr/bin/python3

import math

print('{}web: {}!'.format('cainiao', 'www.baidu.com'))
print('{0:2d}web: {1:.3f}'.format(23123, math.pi))

str = input("input:")
print("input is %s"% str)

print("-------------file------------------")
f = open(str, "w")
f.write('good\npython\nhello world\n')
f.close

with open(str, "r") as f:
    s = f.read()
    print(s)
