import socket
import os
from threading import *

os.system("color 0e")
def sender(server_ip,server_port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    name  = input("\n\t\ttype your name : ")
    print(f"\t\tWelcome to chat room {name} (to quit type : q)")
    while True :
        data = input("\t\tmsg : ")
        data = f"{name} : " + data
        # print("\t\t",data)
        s.sendto(data.encode(),(server_ip,server_port))

def reciever(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,port))
    while True:
        data = s.recvfrom(1024)
        print("\t\t",data[0].decode())

ip  = "192.168.99.1"
port = 2222

server_ip = "192.168.56.101"
server_port = 2222

Thread(target=sender,args=(server_ip,server_port)).start()
Thread(target=reciever,args=(ip,port)).start()

