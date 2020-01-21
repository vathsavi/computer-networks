import socket
import random
from ast import literal_eval

N = 25
rando = []
for i in range(N):
    rando.append(random.randint(1,100))


s = socket.socket()
host = socket.gethostname()
portc = 32451
ports = 12345

s.bind((host,portc))

s.connect((host,ports))
print (s.recv(1024))
s.send(b'It was nice talking to you')
print(rando)
s.send(bytes(str(rando),'UTF-8'))
temp = s.recv(N*1024).decode('utf-8')
out = literal_eval(temp)
print('\ncommon array: ',out)
temp2 = s.recv(N*1024).decode('utf-8')
sorta = literal_eval(temp2)
print('\nsorted: ',sorta)
s.close() 