# BWhacker

![Banner](https://github.com/abebaw977/BWhacker/blob/main/banner.jpg)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Ethics & Legal Notice](#ethics--legal-notice)
3. [Installation](#installation)
4. [Repository Structure](#repository-structure)
5. [Core Modules](#core-modules)
    - [Banner.py (Launcher)](#bannerpy-launcher)
    - [Attacking Suite (P1–P20)](#attacking-suite-p1p20)
    - [Dribs Directory Brute-Forcer](#dribs-directory-brute-forcer)
    - [Steganography Tools](#steganography-tools)
    - [Reverse Shells](#reverse-shells)
    - [Web Scraping Automation](#web-scraping-automation)
    - [Developer Utilities](#developer-utilities)
    - [Database & Vulnerable Login](#database--vulnerable-login)
6. [Advanced Usage](#advanced-usage)
7. [Sample Workflows](#sample-workflows)
8. [Extensive Examples](#extensive-examples)
9. [Customization & Extension](#customization--extension)
10. [Module API Reference](#module-api-reference)
11. [Troubleshooting & FAQ](#troubleshooting--faq)
12. [Contributing](#contributing)
13. [License](#license)
14. [Credits](#credits)
15. [Appendix: Output Snapshots](#appendix-output-snapshots)
16. [Appendix: Test Scenarios](#appendix-test-scenarios)
17. [Appendix: Developer Notes](#appendix-developer-notes)
18. [Appendix: Full Example Scripts](#appendix-full-example-scripts)

---

## Project Overview

**BWhacker** is an advanced, modular Python toolkit for security research, penetration testing, network analysis, password attacks, steganography, phishing simulation, web automation, and developer productivity.  
The toolkit is designed to be both accessible for learners and powerful for professionals, with a focus on extensibility, interactive usage, and deep feature coverage.

---

## Ethics & Legal Notice

> **WARNING:**  
> This toolkit is intended for educational purposes and authorized security testing only.  
> Unauthorized use against systems without explicit permission is illegal and unethical.  
> By using BWhacker, you agree to comply with all applicable laws and ethical guidelines.

---

## Installation

### Requirements

- Python 3.8+
- pip
- MySQL (for database modules)
- Optional: GCC/C++ (for developer utilities)
- Optional: scapy (for packet manipulation)
- Optional: Flask (for web modules)
- Optional: Pillow & wave (for steganography)

### Install AbuColor (for colored output)

```bash
pip install abu-color
```

### Clone the Repository

```bash
git clone https://github.com/abebaw977/BWhacker.git
cd BWhacker
```

### Install Additional Dependencies

```bash
pip install requests rich flask mysql-connector-python pillow tqdm scapy aiohttp
```

### Run the Interactive Launcher

```bash
sudo python3 Hacker/Banner.py
```

> *`sudo` is required for some modules (packet sniffing, ARP spoofing, WiFi attacks).  
> Run as root only on your own test lab or with explicit permission.*

---

## Repository Structure

```
BWhacker/
│
├── Hacker/
│   ├── Banner.py                # Main interactive launcher
│   ├── dribs.py                 # Directory brute-forcer
│   └── Attacking/
│       ├── P1PortScan.py              # Async port scanner
│       ├── P2SubDomainFinder.py       # Subdomain reconnaissance
│       ├── P4HttpFuzzer.py            # HTTP endpoint fuzzer
│       ├── P5BruitForceDirectory.py   # Directory brute-forcer
│       ├── P6ScapySniffLocal.py       # Packet sniffing
│       ├── P7ArpSpoofing.py           # ARP spoofing
│       ├── P8HashPasswordCrack.py     # Hash password cracking
│       ├── P9PasswordGen.py           # Password generator
│       ├── P10WebRecon.sh             # Bash web recon script
│       ├── P11BruiteForceLogin.py     # Login brute-force
│       ├── P12WifiDeauth.py           # WiFi deauthentication attack
│       ├── P13ReverseAttacker.py      # Reverse shell attacker
│       ├── P13ReverseVictim.py        # Reverse shell victim
│       ├── P14SqlInjection.py         # SQL injection
│       ├── P16PasswordManager.py      # Password manager
│       ├── P17AdvancedArpSpoofing.py  # Advanced ARP spoofing/sniffing
│       ├── P18Steganography.py        # Steganography (image/audio)
│       ├── P19AdvReverseAt.py         # Advanced reverse attacker (file transfer, control)
│       ├── P19AdvReverseVi.py         # Advanced reverse victim
│       ├── P20PhishingStimulation.py  # Phishing simulation module
│       ├── DataBase.py                # MySQL database setup
│       ├── VulnLogin.py               # Vulnerable login for testing
│   ├── ScrapWeb.py              # Web scraper
│   ├── DeveloperOptions/
│       ├── Tree.py
│       ├── CppRunner.py
│       └── Extractor.py
│
├── banner.jpg                   # Project banner image
└── README.md                    # This file
```

---

## Core Modules

### Banner.py (Launcher)

The interactive CLI launcher for all modules, with dynamic menus and colored output using AbuColor.

- **Features:**  
    - ASCII art banner, colored UI  
    - User input handling, error management  
    - Loops until user exits  
    - Imports & executes all attack, phishing, utility, and developer scripts  
    - Launches Bash scripts for web reconnaissance

**Example Main Menu:**
```
[1] Attacking Tools
[2] Sniff Tools
[3] Web Tools
[4] Developer Tools
[0] Exit
```

---

### Attacking Suite (P1–P20)

A collection of advanced penetration testing modules. Now including:

- **P20PhishingStimulation.py:** Simulate phishing attacks for training, awareness, and testing.  
  _Features:_ Email spoofing, fake login page generation, credential capture (test/lab), reporting.

Other modules span:

- Port scan, subdomain enumeration, HTTP fuzzing, directory brute-force, hash cracking, password generation, login brute-force, SQL injection, reverse shells, password manager, steganography (image/audio), ARP/WiFi attacks, advanced reverse/file transfer, and more.

---

### Dribs Directory Brute-Forcer

Multithreaded brute-forcing of web directories using custom wordlists.  
Auto-detects environment (Termux, Userland, Linux, local).

---

### Steganography Tools

Hide and reveal messages in images (.png, .bmp) and audio (.wav).

---

### Reverse Shells

Classic and advanced reverse shells, including bidirectional command/control, file upload/download, and persistent logging.

---

### Web Scraping Automation

Targeted web scraping, URL extraction, and content search with ScrapWeb.py.

---

### Developer Utilities

- C++ runner (compile & run C++ from CLI)
- File tree search
- Universal file extractor

---

### Database & Vulnerable Login

- MySQL integration for lab environments
- Vulnerable login system for SQLi testing and training

---

## Advanced Usage

All modules can be executed interactively via Banner.py or imported and used directly in Python scripts.

**Example:**  
```python
from Attacking.P20PhishingStimulation import PhishingAttack
PhishingAttack()
```

---

## Sample Workflows

### Example 1: Full Pen-Test Chain

```python
from Attacking.P2SubDomainFinder import SubDomain
from Attacking.P1PortScan import PortScan
from Attacking.P5BruitForceDirectory import BruiteForceDir
from Attacking.P4HttpFuzzer import HttpFuzzer
from Attacking.P14SqlInjection import SqlAtcking
from Attacking.P11BruiteForceLogin import BrutForceLogin
from Attacking.P8HashPasswordCrack import HashPassC
from Attacking.P9PasswordGen import PasswordGen
from Attacking.P13ReverseAttacker import ReverseAttacker
from Attacking.P13ReverseVictim import RreverseVictim

SubDomain("target.com")
PortScan("target.com")
BruiteForceDir("target.com")
HttpFuzzer()
SqlAtcking("target.com/login")
BrutForceLogin()
HashPassC("hashes.txt", "wordlist.txt")
PasswordGen()
ReverseAttacker()
RreverseVictim()
```

### Example 2: Directory Brute-Force with Dribs

```python
from Hacker.dribs import dribsAttack
dribsAttack()
```

### Example 3: Steganography

```python
from Attacking.P18Steganography import HideData, DecodeI
HideData("input.png", "Secret message", "output.png")
DecodeI("output.png")
```

### Example 4: Phishing Simulation (P20)

```python
from Attacking.P20PhishingStimulation import PhishingAttack
PhishingAttack()
```

### Example 5: C++ Developer Utility

```python
from DeveloperOptions.CppRunner import CppDev
CppDev()
```

### Example 6: WiFi Deauthentication

```python
from Attacking.P12WifiDeauth import WifiDeauth
WifiDeauth()
```

### Example 7: SQL Injection Vulnerability Test

```python
from Attacking.VulnLogin import login
login()
```

### Example 8: Web Scraping

```python
from ScrapWeb import ScrapRunner
ScrapRunner()
```

### Example 9: Advanced Reverse Shell File Transfer

```python
from Attacking.P19AdvReverseAt import ReverseAttacker
from Attacking.P19AdvReverseVi import ReverseV

ReverseAttacker()
ReverseV()
```

### Example 10: ARP Spoofing

```python
from Attacking.P7ArpSpoofing import ArpSpoof
ArpSpoof()
```

### Example 11: Password Management

```python
from Attacking.P16PasswordManager import PasswordManagers
PasswordManagers()
```

### Example 12: Extractor Utility

```python
from DeveloperOptions.Extractor import extractor_file
extractor_file()
```

### Example 13: Tree Search Utility

```python
from DeveloperOptions.Tree import TreeSearch
TreeSearch()
```

---

## Extensive Examples

### CLI Example: Using Banner.py

```bash
sudo python3 Hacker/Banner.py
```
_Navigate the interactive menu and select tools to run._

---

### Output Example: Password Generator

```text
Enter password length: 16
Enter options (letter=y, symbol=y, num=y): y y y
[*] Generated password: aB8@#zLq2!Xv9LmN
[*] Password strength: Very strong password
[*] Cracking time: 127.38 years => BlackHacker
```

### Output Example: Directory Brute-Force

```text
Url : http://testphp.vulnweb.com/
***** [green][bold]admin[bold][/green]
***** [green][bold]images[bold][/green]
Enter file (use above files): admin.txt
[+] Gine Acsess From: http://testphp.vulnweb.com/admin
[X] Not Found: http://testphp.vulnweb.com/backup
...
```

### Output Example: Reverse Shell

```text
Enter port: 4444
[+] listening ....
[*] Connected from: ('192.168.1.10', 52345)
$: whoami
root
$: upload secret.txt
[+] secret.txt uploaded successfully.
$: download secrets.db
[*] secrets.db file is Saved
```

### Output Example: Steganography

```text
[*] Message hidden in image: output.png
[**] Hidden MSG: This is a secret!
```

### Output Example: Web Scraper

```text
Enter URL: https://example.com
[*] Found 42 links containing 'https'
[*] Search for: 'login'
[*] Found: login page at /login
```

### Output Example: Phishing Simulation

```text
[*] Phishing email template generated!
[*] Fake login page running at http://localhost:8888
[*] All captured credentials saved in phishing_results.txt
```

### Output Example: WiFi Deauth

```text
Network status
Route table...
Interface: wlan0
Our IP: 192.168.1.101
Our MAC: 00:11:22:33:44:55
Gateway IP: 192.168.1.1
Gateway MAC: aa:bb:cc:dd:ee:ff
[*] Devices on subnet 192.168.1.0/24:
IP: 192.168.1.1, MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.101, MAC: 00:11:22:33:44:55
[*] Total devices found: 2

Send deauth packets? This will disconnect your device. (y/n): y
[+] Deauth packets sent!
```

---

## Customization & Extension

- Add new scripts to Hacker/Attacking or DeveloperOptions
- Update Banner.py to include new menu entries
- Use AbuColor for consistent UI
- Extend wordlist detection in dribs.py as needed

---

## Module API Reference

Please see individual `.py` files for API signatures and usage examples.  
Key modules:  
- PortScan(), SubDomain(), HttpFuzzer(), BruiteForceDir(), HashPassC(), PasswordGen(), BrutForceLogin(), SqlAtcking(), ReverseAttacker(), ReverseV(), PasswordManagers(), SryphtoSecretData(), PhishingAttack(), etc.

---

## Troubleshooting & FAQ

- **Sudo required?** For packet/sniffing/ARP/WiFi modules.
- **MySQL errors?** Ensure server is up, creds are correct, dependencies installed.
- **Phishing module?** Use only in test/lab, never for real attacks.
- **Custom wordlists?** Place in detected wordlist directory; see dribs.py.
- **Banner.py won’t start?** Check dependencies, paths, permissions.

---

## Contributing

- Fork, branch, PRs welcome
- Issues for bugs, requests, ideas
- Follow strong Python and security best practices

---

## License

BSD 3-Clause "New" or "Revised" License  
See [LICENSE](LICENSE).

---

## Credits

- Project by [abebaw977](https://github.com/abebaw977)
- AbuColor by [abu-color](https://pypi.org/project/abu-color/)
- Inspired by open-source hacking tools and CTF labs.

---

## Appendix: Output Snapshots

### PasswordGen Output

```text
Enter password length: 12
Enter options (eg, letter=y or n, symbol=..., num=...): y y y
[*] Generated password: aB8@#zLq2!Xv
[*] Password strength: Very strong password
[*] Cracking time: 7.73 years => BlackHacker
```

### Dribs Brute-Force Output

```text
Url : http://testphp.vulnweb.com/
***** [green][bold]admin[bold][/green]
***** [green][bold]images[bold][/green]
Enter file (use above files): admin.txt
[+] Gine Acsess From: http://testphp.vulnweb.com/admin
[X] Not Found: http://testphp.vulnweb.com/backup
...
```

### Reverse Shell Output

```text
Enter port: 4444
[+] listening ....
[*] Connected from: ('192.168.1.10', 52345)
$: whoami
root
$: upload secret.txt
[+] secret.txt uploaded successfully.
$: download secrets.db
[*] secrets.db file is Saved
```

### Steganography Output

```text
[*] Message hidden in image: output.png
[**] Hidden MSG: This is a secret!
```

### Web Scraper Output

```text
Enter URL: https://example.com
[*] Found 42 links containing 'https'
[*] Search for: 'login'
[*] Found: login page at /login
```

### Phishing Simulation Output

```text
[*] Phishing email template generated!
[*] Fake login page running at http://localhost:8888
[*] All captured credentials saved in phishing_results.txt
```

---

## Appendix: Test Scenarios

- Run Banner.py and interactively select each module.
- Use Dribs for directory brute-forcing with custom wordlists.
- Generate and crack passwords with PasswordGen and HashPasswordCrack.
- Create, receive, and manage reverse shell connections.
- Test SQL injection with VulnLogin.
- Hide and reveal secret messages in images/audio.
- Simulate phishing attacks with P20 in a safe lab.
- Use developer utilities for file search, C++ compilation, and extraction.

---

## Appendix: Developer Notes

- All modules are Python scripts and can be imported.
- Banner.py is the main orchestrator.
- AbuColor is used for enhanced CLI visuals.
- Wordlists and test data should be placed as per module requirements.
- Phishing, ARP, WiFi, and packet modules require root/admin.

---

## Appendix: Full Example Scripts

### Full Recon and Attack

```python
from Attacking.P2SubDomainFinder import SubDomain
from Attacking.P1PortScan import PortScan
from Attacking.P5BruitForceDirectory import BruiteForceDir
from Attacking.P4HttpFuzzer import HttpFuzzer
from Attacking.P14SqlInjection import SqlAtcking
from Attacking.P11BruiteForceLogin import BrutForceLogin
from Attacking.P8HashPasswordCrack import HashPassC
from Attacking.P9PasswordGen import PasswordGen
from Attacking.P13ReverseAttacker import ReverseAttacker
from Attacking.P13ReverseVictim import RreverseVictim
from Attacking.P18Steganography import HideData, DecodeI
from Attacking.P20PhishingStimulation import PhishingAttack

SubDomain("target.com")
PortScan("target.com")
BruiteForceDir("target.com")
HttpFuzzer()
SqlAtcking("target.com/login")
BrutForceLogin()
HashPassC("hashes.txt", "wordlist.txt")
PasswordGen()
ReverseAttacker()
RreverseVictim()
HideData("input.png", "Secret message", "output.png")
DecodeI("output.png")
PhishingAttack()
```

---

*This README is designed to be a full, practical reference for BWhacker users and contributors. For code updates, documentation, and the latest features, visit [BWhacker on GitHub](https://github.com/abebaw977/BWhacker).*
