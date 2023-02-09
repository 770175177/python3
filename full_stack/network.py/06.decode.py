#!/usr/bin/python3

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

bindAddr = ('',7788)
udpSocket.bind(bindAddr)

recvData = udpSocket.recvfrom(1024) #recv max size 1024
contend, dstInfo = recvData

print('recv: %s'%contend.decode('gb2312'))  


udpSocket.close()
