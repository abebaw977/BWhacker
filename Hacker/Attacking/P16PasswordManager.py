import json
import string
import random
import os
from rich.console import Console
from rich.table import Table

File="PasswordManager.json"
array=[]
def generate_password():
    punc="(!@#$%^&*)"
    return "".join(random.sample(string.ascii_letters+string.digits+punc,k=32))
def search_entry():
    Site=input("Enter site: ").strip()
    try:
        with open(File, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    F=False
    for s in data:
        if Site.lower() == s["site"].lower():
            print(f"[@] Site: {s["site"]}")
            print(f"[&] Username: {s["username"]}")
            print(f"[?] Password: {s["password"]}")
            F=True
    if not F:
        print(f"[!] Not exists( --> {Site}")
def add_entry():
    site = input("Site: ")
    username = input("Username: ")
    pw_choice = input("Enter password or generate? (e/g): ").lower()
    if pw_choice == 'g':
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        password = input("Password: ")
    try:
        with open(File, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(
        {
            "site": site,
            "username": username,
            "password": password
        }
    )
    with open(File, "w") as j:
        json.dump(data, j, indent=2)

    print("Entry added successfully!")
def delete_entry():
    site=input("Enter site: ").strip()
    F=False
    try:
        with open(File, "r") as f:
            a = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        a = []
    for l,s in enumerate(a):
        if site.lower() == s["site"].lower():
            a.pop(l)
            F=True
    try:
        if F:
            os.system(f"rm {File}")
            with open(File, "w") as j:
                json.dump(a, j, indent=2)
                print("File is updated")
        else:print(f"[!] Not exists --> ${site}")
    except (FileNotFoundError, json.JSONDecodeError):
        pass
def edit_entry():
    site = input("Site: ")
    F=False
    try:
        with open(File, "r") as f:
            a = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        a = []
    for l,s in enumerate(a):
        if site.lower() == s["site"].lower():
            username = input("Username: ")
            pw_choice = input("Enter password or generate? (e/g): ").lower()
            if pw_choice == 'g':
                password = generate_password()
                print(f"Generated password: {password}")
            else:
                password = input("Password: ")
            if not password or not username:
                print("[!] Please enter full value (pass or user) !!")
                return
            a.pop(l)
            a.append(
                {
                    "site": site,
                    "username": username,
                    "password": password
                }
                )
            with open(File, "w") as j:
                json.dump(a, j, indent=2)
            print(f"[+] {site} :This site Updated")
            F=True
    if not F:
        print(f"[!] Not exists --> ${Site}")
def show_entry():
    console = Console()
    table = Table(title="Password Manager")

    table.add_column("Id", justify="right", style="cyan", no_wrap=True)
    table.add_column("UserName", style="magenta")
    table.add_column("site", justify="right", style="green")
    table.add_column("password")
    try:
        with open(File, "r") as f:
            a = json.load(f)
        for l,s in enumerate(a,start=1):
            table.add_row(str(l),s["username"],s["site"],s["password"])
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    console.print(table)
def PasswordManagers():
    while True:
        print("\n------- Password Manager -------")
        print("1. Add Entry")
        print("2. Search Entry")
        print("3. Edit Entry")
        print("4. Delete Entry")
        print("5. Show Data")
        print("6. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entry()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            show_entry()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
