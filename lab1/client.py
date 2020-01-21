import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name/for this example
ports = 12345             #server port
portc = 32451 	   #client's own port for incoming connections (if any)
s.bind((host, portc))
s.connect((host, ports))
print (s.recv(1024))
s.send(b'nice')
s.close                     # Close the socket when done
