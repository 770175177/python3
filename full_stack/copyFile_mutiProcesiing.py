#!/usr/bin/python3

from multiprocessing import Pool,Manager
import os

def copyFileTask(name, oldFolserName, newFolderName, queue):
	fr = open(oldFolserName+'/'+name)
	fw = open(newFolderName+'/'+name,'w')
#	print('----%shas been copyed'%name)
	content = fr.read()
	fw.write(content)

	fr.close()
	fw.close()

	queue.put(name)

def main():
	#0. get old folder name
	oldFolserName = input("put folder name:")

	#1. creat FileFolder
	newFolderName = '[copy]-' + oldFolserName
	#print(newFolderName)
	os.mkdir(newFolderName)

	#2. get all the old filenames
	fileNames = os.listdir(oldFolserName)
#	print(fileNames)

	#3. use MutiPocessing copy old files to new folder
	pool = Pool(5) 
	queue = Manager().Queue()

	for name in fileNames:
		pool.apply_async(copyFileTask, args=(name, oldFolserName, newFolderName, queue))

#	pool.close()
#	pool.join()
	num = 0
	allNum = len(fileNames)
	while num<allNum:
		queue.get()
		num += 1
		copyRate = num / allNum
		print('\rcopy rate is: %.2f%%'%(copyRate*100),end = '')
#		if num == allNum:
#			break
	print("\ncomplet!")

if __name__ == '__main__':
	main()
