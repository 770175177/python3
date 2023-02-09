#!/usr/bin/python3

import os

file_list = os.listdir('./test')
#print(file_list)
os.chdir('./test')
for name in file_list:
	os.rename(name,'[jindong]'+name)
