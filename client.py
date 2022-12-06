from email import message
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",55555))
s.recv(1024)
s.close()

print(message.decode())
