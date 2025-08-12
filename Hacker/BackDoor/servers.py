import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",4443))
s.listen(5)
conn,addr=s.accept()
print("[*] Connected from: ",addr)
while True:
    data = input("$: ")
    conn.send(data.encode())

    data = conn.recv(4096)
    print(data.decode())