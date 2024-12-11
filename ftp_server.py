import socket
server=socket.socket()
host=socket.gethostname()
port=2345
server.bind((host,port))
server.listen(2)

c,addr=server.accept()
print('get connection:',addr)
data=c.recv(1024).decode('utf-8')
print(data)
# server.send(data,'utf-8')

