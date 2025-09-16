import random
import string
import re
import sys

def PasswordGen():
    try:
        leng = int(input("Enter password length: "))
    except:
        print("Please enter only number!!")
        sys.exit()

    password = input("Enter options (eg, letter=y or n, symbol=..., num=...): ").split()
    letter = string.ascii_letters
    symbol = "!@#.%_+=;:,.<>/?"
    number = string.digits

    p = ""
    if len(password) > 0 and "y" in password[0]:
        p += letter
    if len(password) > 1 and "y" in password[1]:
        p += symbol
    if len(password) > 2 and "y" in password[2]:
        p += number

    def CheackStrength(pw):
        strength = 0
        if re.search(f'[{letter}]', pw):
            strength += 1
        if re.search(f'[{symbol}]', pw):
            strength += 1
        if re.search(f'[{number}]', pw):
            strength += 1
        if strength == 1:
            return "Weak password"
        elif strength == 2:
            return "Strong password"
        elif strength == 3:
            return "Very strong password"
        else:
            return "Unknown strength"

    def crackingTime(Pleng, wLeng, w=1e9):
        C = wLeng ** Pleng
        seconds = C / w
        if seconds < 60:
            return f"{seconds:.2f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.2f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.2f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.2f} days"
        else:
            return f"{seconds/31536000:.2f} years"

    if p:
        Password = "".join(random.choice(p) for _ in range(leng))
        print("[*] Generated password: {}".format(Password))
        print("[*] Password strength: {}".format(CheackStrength(Password)))
        print("[*] Cracking time: {} => BlackHacker".format(crackingTime(len(Password), len(p))))
    else:
        print("[?] No option selected")

