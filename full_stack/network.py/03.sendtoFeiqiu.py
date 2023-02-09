#coding=utf-8

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('192.168.126.129',2425)

sendData = raw_input('please input data:')
sendData = '1:1238605487:user:machime:32:' + sendData
print sendData
#sendData = sendData.encode(encoding='utf-8')

udpSocket.sendto(sendData, sendAddr)

udpSocket.close()
