import socket

host = "localhost"
port = 8000

mySocket = socket.socket()
mySocket.connect((host,port))


mySocket.send("Hola desde el cliente".encode())
print(mySocket.recv(1024))
mySocket.close()
