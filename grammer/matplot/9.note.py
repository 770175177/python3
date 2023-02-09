#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#create data
fig = plt.figure(dpi=80)	#create a chart
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.xlabel("x axe")
plt.ylabel("Y axe")
plt.title("sin(x) function")
#plt.legend()

plt.show()	#show all charts
