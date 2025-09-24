import pickle
import socket

s = socket.socket()

hostname = socket.gethostname()
portno = 50000

s.connect((hostname, portno))
std1 = s.recv(1024)
std2 = pickle.loads(std1)
print(std2)
s.close()