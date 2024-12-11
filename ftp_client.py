import socket
client=socket.socket()
host=socket.gethostname()
port=2345
client.connect((host,port))
file=open('client.txt','r')
data=file.read()
# print(data)
client.send(bytes(data,'utf-8'))
data=client.recv(1024).decode('utf-8')
print(data)

f=open('recv.txt','w')
f.write(data)