#!/usr/bin/python3

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('127.0.0.1', 7788)

sendData = input('please input data:')
sendData = sendData.encode(encoding='utf-8')

udpSocket.sendto(sendData, sendAddr)

udpSocket.close()
