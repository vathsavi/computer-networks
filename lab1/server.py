import socket               # Import socket module
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
    check={}
    dup=[]
    for x in l:
        if x not in check:
            check[x]=1
        else:
            if check[x]==1:
                dup.append(x)
            
    temp = list(dict.fromkeys(l)) 
    c.send(bytes(str(temp),'UTF-8'))
    c.send(bytes(str(check  ),'UTF-8'))
    c.close()                # Close the connection
