import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port=9001
server.bind((host,port))
msg,addr=server.recvfrom(1024)
msg=msg.decode('utf-8')
print(msg)

newmsg=msg.upper()
newmsg=newmsg.encode('utf-8')
server.sendto(newmsg,addr)