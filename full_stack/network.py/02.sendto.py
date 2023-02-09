#!/usr/bin/python3

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('192.168.126.1',8080)

sendData = input('please input data:')
sendData = sendData.encode(encoding='utf-8')

udpSocket.sendto(sendData, sendAddr)

udpSocket.close()
