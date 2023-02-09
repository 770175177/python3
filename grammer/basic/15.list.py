#!/usr/bin/python3

t = ['adc', 'db', 'c', 'd', 'e']
print(t)
print(t[2:])
print(t[2:-1])
print(t + t)
print('------------')
t[0] = 'b'
t.append('c')
print(t)
t.pop()
print(t)
print(t[1:4:2])
