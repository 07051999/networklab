import socket
UDP_IP_ADDRESS="10.1.24.128"
UDP_PORT_NO=6789
Message=("hello world")
bytesTosend=str.encode(Message)
clientsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsock.sendto(bytesTosend,(UDP_IP_ADDRESS,UDP_PORT_NO))
