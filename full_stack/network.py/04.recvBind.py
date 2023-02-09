#!/usr/bin/python3

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

bindAddr = ('',7788)
udpSocket.bind(bindAddr)

recvData = udpSocket.recvfrom(1024) #recv max size 1024
print(recvData)  

#udpSocket.sendto('recv:go on!')

udpSocket.close()
