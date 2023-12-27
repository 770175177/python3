#!/usr/bin/python3
import sys

while True:
    try:
        x = int(input("input a number: "))
        break
    except ValueError:
        print("input is not a number, try!")

try:
    f = open('foo.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer")
except:
    print("Unexcepted error: ", sys.exc_info()[0])
    raise
else:
    print("success: no error!")
    f.close()
finally:
    print("finally: it will excute anymore")

x = 10
if x > 5:
    raise Exception('x={} is bigger than 5'.format(x))
