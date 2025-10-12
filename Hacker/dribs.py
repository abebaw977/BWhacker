import requests
from rich.console import Console
from pathlib import Path
import time
from concurrent.futures import ThreadPoolExecutor
import sys
import os

c = Console()

def detect_wordlist_dir():
    termux_path = "/data/data/com.termux/files/usr/share/dirb/wordlists/"
    userland_path = "/home/userland/Enviroments/dirb16/wordlists/"
    
    if Path(termux_path).exists():
        c.print("[green]✓ Detected Termux environment[/green]")
        return termux_path
    elif Path(userland_path).exists():
        c.print("[green]✓ Detected Userland environment[/green]")
        return userland_path
    else:
        common_paths = [
            "/usr/share/dirb/wordlists/",
            "/usr/share/wordlists/dirb/",
            "/opt/dirb/wordlists/",
            "./wordlists/"
        ]
        
        for path in common_paths:
            if Path(path).exists():
                c.print(f"[green]✓ Found wordlists at: {path}[/green]")
                return path
        
        c.print("[yellow]⚠ No standard wordlist directory found. Using current directory.[/yellow]")
        return "./"

dirbsFile = detect_wordlist_dir()
FU = []
dtarget = ""

def dribsAttack():
    Found = 0
    redi = 0
    global dtarget
    
    dtargets = input("Enter url: ").strip()
    
    if not dtargets:
        dtargets = "http://testphp.vulnweb.com/"
        c.print(f"[yellow]Using default target: {dtargets}[/yellow]")
    
    if not dtargets.startswith(('http://', 'https://')):
        dtargets = "https://" + dtargets
        c.print(f"[yellow]Added protocol: {dtargets}[/yellow]")
    
    if not dtargets.endswith("/"):
        dtarget = dtargets + "/"
    else:
        dtarget = dtargets
    
    c.print(f"[green]Target URL: {dtarget}[/green]")
    
    wordlist_dir = Path(dirbsFile)
    
    if not wordlist_dir.exists():
        c.print(f"[red]Error: Directory {dirbsFile} not found![/red]")
        c.print("[yellow]Please make sure dirb is installed or specify correct path.[/yellow]")
        return
    
    files = list(wordlist_dir.glob("*"))
    flist = []
    
    for file in files:
        if file.is_file():
            f = file.name
            flist.append(f)
    
    if not flist:
        c.print(f"[red]No wordlist files found in {dirbsFile}![/red]")
        c.print("[yellow]Available directories:[/yellow]")
        for item in wordlist_dir.iterdir():
            if item.is_dir():
                c.print(f"[F] {item.name}/")
        return
    
    c.print(f"\n[bold][green]Available Wordlists ({len(flist)}):[/green][/bold]")
    flist.sort()
    for i, f in enumerate(flist[:20]):
        c.print(f"  [{i+1}] {f}")
    
    if len(flist) > 20:
        c.print(f"  ... and {len(flist) - 20} more files")
    
    rep = True
    while rep:
        ftarget = input("\nEnter filename (or number from list): ").strip()
        
        if not ftarget:
            common_defaults = ["common.txt", "big.txt", "small.txt", "indexes.txt"]
            for default in common_defaults:
                if default in flist:
                    ftarget = default
                    c.print(f"[yellow]Using default file: {ftarget}[/yellow]")
                    rep = False
                    break
            else:
                ftarget = flist[0] if flist else ""
                c.print(f"[yellow]Using first available file: {ftarget}[/yellow]")
                rep = False
        else:
            if ftarget.isdigit():
                index = int(ftarget) - 1
                if 0 <= index < len(flist):
                    ftarget = flist[index]
                    rep = False
                else:
                    c.print(f"[red]Invalid number. Please choose between 1-{len(flist)}[/red]")
            elif ftarget in flist:
                rep = False
            else:
                c.print("[red]File not found in list. Please choose from available files.[/red]")
                c.print("[yellow]Tip: You can use the number from the list instead of full filename.[/yellow]")
    
    path = wordlist_dir / ftarget
    try:
        with open(path, "r", encoding='utf-8', errors='ignore') as f:
            attacks = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        c.print(f"[red]Error: File {path} not found![/red]")
        return
    except Exception as e:
        c.print(f"[red]Error reading file: {e}[/red]")
        return
    
    if not attacks:
        c.print("[red]No words found in the wordlist file![/red]")
        return
    
    c.print(f"[green]Loaded {len(attacks)} words from {ftarget}[/green]")
    
    def Hack(url):
        nonlocal Found, redi
        try:
            r = requests.get(url, timeout=10, allow_redirects=False)
            
            if r.status_code == 200:
                c.print(f"[green][+] Found ({r.status_code}): {url}[/green]")
                FU.append(url)
                Found += 1
            elif r.status_code in [301, 302, 307, 308]:
                c.print(f"[yellow][→] Redirect ({r.status_code}): {url}[/yellow]")
                redi += 1
            elif r.status_code == 403:
                c.print(f"[red][-] Forbidden ({r.status_code}): {url}[/red]")
            elif r.status_code == 401:
                c.print(f"[blue][!] Unauthorized ({r.status_code}): {url}[/blue]")
            elif r.status_code == 404:
                pass
            elif r.status_code == 500:
                c.print(f"[red][!] Server Error ({r.status_code}): {url}[/red]")
            else:
                c.print(f"[blue][?] Status {r.status_code}: {url}[/blue]")
                
        except requests.exceptions.Timeout:
            c.print(f"[red][×] Timeout: {url}[/red]")
        except requests.exceptions.ConnectionError:
            c.print(f"[red][×] Connection Error: {url}[/red]")
        except Exception as e:
            c.print(f"[red][×] Error checking {url}: {e}[/red]")
    
    url_list = [dtarget + attack for attack in attacks]
    
    c.print(f"[yellow]Starting scan with {len(url_list)} URLs...[/yellow]")
    c.print(f"[yellow]Using {min(50, len(url_list))} workers[/yellow]")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        chunk_size = 100
        for i in range(0, len(url_list), chunk_size):
            chunk = url_list[i:i + chunk_size]
            executor.map(Hack, chunk)
            progress = min(i + chunk_size, len(url_list))
            c.print(f"[blue]Progress: {progress}/{len(url_list)} ({progress/len(url_list)*100:.1f}%)[/blue]")
    
    end_time = time.time()
    
    c.print(f"\n[bold][green]Scan completed in {end_time - start_time:.2f} seconds[/green][/bold]")
    c.print(f"[yellow][bold]Found: {Found}[/bold][/yellow]")
    c.print(f"[cyan][bold]Redirects: {redi}[/bold][/cyan]")
    
    if FU:
        c.print(f"\n[green][bold]Discovered URLs ({len(FU)}):[/bold][/green]")
        for fu in FU:
            c.print(f"  [green]{fu}[/green]")
    else:
        c.print("[yellow]No URLs discovered.[/yellow]")


