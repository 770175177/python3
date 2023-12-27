#!/usr/bin/python3

x = lambda a: a + 10
print(x(5))

sum = lambda arg1, arg2: arg1 + arg2
print("sum %d + %d = %d"% (10, 22, sum(10, 22)))

f = lambda: 'Hello, world!'
print(f())
