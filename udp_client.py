import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=socket.gethostname()
port=9001
msg=input("enter your message:")
address=(host,port)
msg=msg.encode('utf-8')
client.sendto(msg,address)
newmsg,addr=client.recvfrom(1024)
newmsg=newmsg.decode('utf-8')
print(newmsg)