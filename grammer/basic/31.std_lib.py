#!/usr/bin/python3

import os           # system option
import sys          # system function
import time         # time 
import datetime     # enhance time
import random       # random function
import math         # math
import re           # regular
import json         # JSON encode and decode
from urllib.request import urlopen       # web
import smtplib      # email
import zlib

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.system("ls -al")
os.chdir('basic')
print(os.getcwd())

print(sys.argv)
sys.stderr.write('Warning, long file not found a new one\n')

print("-----------------------------------")
print(re.findall(r'\bf[a-z]*', 'which food or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print("-----------------------------------")
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print("-----------------------------------")
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

print("-----------------------------------")
for line in urlopen('https://www.baidu.com'):
    line = line.decode('utf-8')
    print(line)

print("-----------------------------------")
#server = smtplib.SMTP('localhost')
#server.sendmail('770175177@qq.com', '770175177@qq.com',
#'''To: 
#From:
#'''
#)
#server.quit()

print("-----------------------------------")
cur = datetime.datetime.now()
print(cur)
fcur = cur.strftime("%Y-%m-%d %H:%M:%S")
print(fcur)
cur = datetime.date.today()
print(cur)

print("-----------------------------------")
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

