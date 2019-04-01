import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                

host = "172.25.37.209"

s.connect((host, port))

for x in range(5):
    print(s.recv(1024).decode())

s.close()                     