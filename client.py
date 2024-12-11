import socket
client=socket.socket()
host=socket.gethostname()
port=1234
client.connect((host,port))
a=client.recv(1024).decode("utf-8")
no1=input('enter no1=')
no1=client.send(bytes(no1,'utf-8'))
no2=input('enter no2=')
no2=client.send(bytes(no2,'utf-8'))
ans=client.recv(1024).decode('utf-8')
print(ans)
print(a)





