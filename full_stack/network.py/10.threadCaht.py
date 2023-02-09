#!/usr/bin/python3

from threading import Thread
from socket import *

def recvData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print('\r>>> %s:%s\n<<<'%(str(recvInfo[1][0]), recvInfo[0].decode('gb2312')), end='')

def sendData():
	while True:
		sendInfo = input("<<<")
		udpSocket.sendto(sendInfo.encode('gb2312'),(dstIP,dstPort))

udpSocket = None
dstIP = ''
dstPort = 0

def main():
	global udpSocket
	global dstIP
	global dstPort

	dstIP = '192.168.126.1'  #input('dstIP:')
	dstPort = 4567         #input('dstPort:')	

	udpSocket = socket(AF_INET,SOCK_DGRAM)
	udpSocket.bind(('',7788))	

	tr = Thread(target=recvData)
	ts = Thread(target=sendData)
	
	tr.start()
	ts.start()
	
	tr.join()
	ts.join()

if __name__ == '__main__':
	main()
