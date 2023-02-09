#!/usr/bin/python3

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind('',69)


