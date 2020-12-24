from django.test import TestCase

# Create your tests here.
from socket import *
serverName = 'DESKTOP-PP68JI4'
serverPort = 12001
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Enter file name")


clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print('From Server:', filecontents)
clientSocket.close()
