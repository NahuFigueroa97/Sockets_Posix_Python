import socket

host = "localhost"
port = 8000

mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(5)

while 1 :
    conexion,direccion = mySocket.accept()
    print("Conectado!!")
    print (direccion)
    conexion.send("Hola desde el servidor".encode())
    print(conexion.recv(1024))
    conexion.close()
    
