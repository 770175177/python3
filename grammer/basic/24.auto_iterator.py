#!/usr/bin/python3

print("list")
li=[i for i in range(30) if i % 3 == 0]
print(li)

print("director")
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

set1 = {i**3 for i in (1, 3, 4)}
print(set1)

tu = (x for x in range(1, 10))
print(tuple(tu))
