#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#create data
data = [100,500,300]
fig = plt.figure(dpi=80)	#create a chart
plt.pie(data,			#actually data
	explode=[0.0,0.0,0.1], 	#distance to certer
	colors=['y','r','g'],	#color of each item
	labels=['A part','B part','C part'],
	labeldistance=1.2,
	autopct='%0.2f%%',	#display format of percent 
	pctdistance=0.4,
	shadow= True,
	startangle=0,
	radius=1
	)

plt.show()	#show all charts
