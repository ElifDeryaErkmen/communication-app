#from http import client
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET means internet socket
#SOCK_STREAM means TCP
#now we need to create listener
s.bind(('127.0.0.1',55555))
s.listen()

while True:
    client, address = s.accept()
    print ("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
