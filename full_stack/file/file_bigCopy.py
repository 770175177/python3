#!/usr/bin/python3

fi = open('./file/test.txt')
fo = open('./file/test_copy.txt', 'w')

fo.write(fi.read(1024))

fi.close()
fo.close()
