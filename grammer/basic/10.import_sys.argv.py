#!/usr/bin/python3

'''
# import somemodule
# from somemodule import somefunction
# from somemodule import firstfunc,secondfunc,thirdfunc
# from somemodule import *
'''

import sys
print('command line parm')
for i in sys.argv:
	print(i)
print('\npathon path', sys.path)
