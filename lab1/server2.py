import socket
import random
from ast import literal_eval


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostbyname(socket.gethostname()) # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print ('host ip', host) 
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    c.send(b'Thank you for connecting')
    print(c.recv(1024))
    l=c.recv(1024).decode('utf-8')
    l=literal_eval(l)
    rando=[]
    for i in range(25):
        rando.append(random.randint(1,100))
    print('\n',rando)

    #check={}
    common=[]
    for x in l:
        if x in rando:
            #check[x]=1
            common.append(x)
        
    
    #temp = list(dict.fromkeys(common)) 
    c.send(bytes(str(common),'UTF-8'))
    common.sort()
    c.send(bytes(str(common ),'UTF-8'))
    
    
    
    
    
    c.close()