import hashlib
import sys
import subprocess

def HashPassC():
    HashV=input("Enter Hash value (eg, md5,sha1,sha256 etc..): ").strip().lower()
    try:
        hashlib.new(f"{HashV}")    
    except:
        print("Wrong hash value,please Enter corrcet hash value !!")
        sys.exit()
    p=input("Enter your password: ")
    pas=hashlib.new(HashV,p.encode()).hexdigest()
    attempt=0
    Found=False
    with open("ethiopia.txt","r",encoding="utf-8") as passwordList:
        for password in passwordList:
            password = password.strip()
            HashP=hashlib.new(HashV)
            HashP.update(password.encode())
            if HashP.hexdigest() == pas:
                print("[*]Found password atampt => {} : password => {} : Hash=>{}".format(attempt,password,HashP.hexdigest()))
                Found=True
                sys.exit()
            attempt+=1
    if not Found:
        print("[!] Password not Found")
