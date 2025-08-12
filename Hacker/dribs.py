import requests
from rich.console import Console
from pathlib import Path
import time
from concurrent.futures import ThreadPoolExecutor

c = Console()


dirbsFile="/home/userland/Enviroments/dirb16/wordlists/"
FU=[]
dtarget=""
def dribsAttack():
    Found =0
    redi=0
    global dtarget
    dtargets=input("Enter url: ")
    if dtargets in [" ",""]: 
        dtargets="http://testphp.vulnweb.com/"
    if not dtargets.endswith("/"):
        dtarget=dtargets+"/"
        print("First: ",dtarget)
    if not dtargets.startswith("http"):
        dtarget="https://"+dtargets
        if not dtargets.endswith("/"):
            dtarget=dtarget+"/"
    if dtarget=="":
        dtarget+=dtargets
    print("Url : ",dtarget)
    files = Path(dirbsFile).glob("*")
    flist=[]
    for file in files:
        t = str(file)
        f=t.replace(dirbsFile," ").strip()
        c.print(f"{'*'*5} [green][bold]{f}[bold][/green]")
        flist.append(f)
    rep=True
    while rep:
      try:
         ftarget=input("Enter file (use above files): ").strip()
         if ftarget in ["",""]: 
            ftarget="a.txt"
            rep = False
         elif ftarget in flist:
            rep=False
      except:
       	 print("File Not Found")
    path =dirbsFile+ftarget
    with open(f"{path}","r") as f:
       attacks = [line.strip() for line in f if line.strip()]
    
    def Hack(url):
        nonlocal Found,redi
        try:
               r = requests.get(url)
               if r.status_code in [200]:
                   c.print(f"[yellow][+] Gine Acsess From[yellow]: [green]{url}[green]")
                   FU.append(url)
                   Found +=1
               elif r.status_code in [302]:
                   print("[*] Redirected")
                   redi +=1
               elif r.status_code == 404:
                   print("[X] Not Found: ",url)
               elif r.status_code == 500:
                   print("[*]Server Error")
               else:
                   print("No")
        except Exception as e:
               print("Something Errors: ",e)
    
    url = [dtarget+attack for attack in attacks]
    with ThreadPoolExecutor(max_workers=100) as excutes:
        excutes.map(Hack,url)
    """
    url_list = [dtarget + attack for attack in attacks]
    for full_url in url_list:
        print(full_url)
    with ThreadPoolExecutor(max_workers=20) as excutes:
        excutes.map(Hack, url_list)"""
    c.print(f"[yellow][bold]Found: {Found}[/bold][green]")
    c.print(f"[green][bold]Redirect: {redi} [/bold][green]")
    for fu in FU:
       c.print(f"[%] Found URL: [green]{fu}[green]")
#dribs()