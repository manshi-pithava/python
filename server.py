import socket
server=socket.socket()
host=socket.gethostname()
port=1234
server.bind((host,port))
server.listen(2)
while True:
    c,addr=server.accept()
    print('getconnection from:',addr)
    c.send(bytes('connection successs..','utf-8'))
    no1=c.recv(1024).decode("utf-8")
    no2=c.recv(1024).decode("utf-8")
    sum=int(no1)+int(no2)
    c.send(bytes(str(sum),'utf-8'))
    print("no1:"+no1)
    print("no2:"+no2)
    print("addtion:",sum)
    c.close()