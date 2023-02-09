#!/usr/bin/python3

from threading import Thread
from socket import *
import time

def recv(udpSocket):
	recvData = udpSocket.recvfrom(1024)
	dstIP = str(recvData[1][0])
	content = recvData[0].decode('gb2312')

	print(str(time.strftime('[%a %b %d %H:%M:%S %Y]', time.localtime()))+' %s : %s'%(dstIP,content))
	return recvData

def main():
	udpSocket = socket(AF_INET, SOCK_DGRAM)

	bindAddr = ('', 7788)

	udpSocket.bind(bindAddr)

	while True:
		recvData = recv(udpSocket)
		udpSocket.sendto(recvData[0],recvData[1])

	udpSocket.close()

if __name__ == '__main__':
	main()
