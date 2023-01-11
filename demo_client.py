import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address='127.0.0.1'
port = 1234
client_socket.connect((ip_address,port))

client_socket.send(b'This is a test')

response = client_socket.recv(1024)
print(response.decode())
