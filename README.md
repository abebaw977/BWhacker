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
    - [Attacking Suite](#attacking-suite)
    - [Dribs Directory Brute-Forcer](#dribs-directory-brute-forcer)
    - [Steganography Tools](#steganography-tools)
    - [Reverse Shells](#reverse-shells)
    - [Web Scraping Automation](#web-scraping-automation)
    - [Developer Utilities](#developer-utilities)
    - [Database & Vulnerable Login](#database--vulnerable-login)
6. [Advanced Usage](#advanced-usage)
7. [Sample Workflows](#sample-workflows)
8. [Customization & Extension](#customization--extension)
9. [Module API Reference](#module-api-reference)
10. [Troubleshooting & FAQ](#troubleshooting--faq)
11. [Contributing](#contributing)
12. [License](#license)
13. [Credits](#credits)

---

## Project Overview

**BWhacker** is an advanced, modular Python toolkit for security research, penetration testing, network analysis, password attacks, steganography, web automation, and developer productivity.  
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
- Optional: GCC/C++ (for developer utilities), scapy (for packet manipulation)

### Install AbuColor (for colored output)

```bash
pip install abu-color
```

### Clone the Repository

```bash
git clone https://github.com/abebaw977/BWhacker.git
cd BWhacker
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
│       ├── P1PortScan.py        # Async port scanner
│       ├── P2SubDomainFinder.py # Subdomain reconnaissance
│       ├── P4HttpFuzzer.py      # HTTP endpoint fuzzer
│       ├── P5BruitForceDirectory.py
│       ├── P8HashPasswordCrack.py
│       ├── P9PasswordGen.py
│       ├── P11BruiteForceLogin.py
│       ├── P13ReverseAttacker.py
│       ├── P13ReverseVictim.py
│       ├── P14SqlInjection.py
│       ├── P16PasswordManager.py
│       ├── P18Steganography.py
│       ├── P19AdvReverseAt.py
│       ├── P19AdvReverseVi.py
│       ├── P6ScapySniffLocal.py
│       ├── P7ArpSpoofing.py
│       ├── P12WifiDeauth.py
│       ├── P17AdvancedArpSpoofing.py
│       └── ... (more)
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

The primary entrypoint for BWhacker is `Banner.py`.  
It provides a dynamic, menu-driven interface to all major modules, categorized into Attacking Tools, Sniff Tools, Web Tools, Developer Tools, and Others.

**Features:**

- ASCII art banner, colored UI (AbuAll)
- Handles user input, numeric choices, error handling
- Loops until user exits
- Imports & executes all attack, utility, and developer scripts
- Launches Bash scripts for web reconnaissance

**Example Main Menu:**

```
[1] Attacking Tools
[2] Sniff Tools
[3] Web Tools
[4] Developer Tools
[0] Exit
```

Selecting a category reveals sub-options mapped directly to core modules.

---

### Attacking Suite

A collection of advanced penetration testing modules, including:

- **P1PortScan.py**: Asynchronous port scanner, scans 20–5000 ports, identifies protocols.
- **P2SubDomainFinder.py**: Finds subdomains of a target domain.
- **P4HttpFuzzer.py**: Fuzzes HTTP endpoints with custom payloads.
- **P5BruitForceDirectory.py**: Brute-forces directories on web servers.
- **P8HashPasswordCrack.py**: Cracks password hashes using wordlists.
- **P9PasswordGen.py**: Generates strong passwords, analyzes strength and crack time.
- **P11BruiteForceLogin.py**: Brute-forces login pages.
- **P13ReverseAttacker.py & P13ReverseVictim.py**: Classic reverse shell implementation.
- **P14SqlInjection.py**: SQL injection attacks for login bypass.
- **P16PasswordManager.py**: Simple password manager.
- **P18Steganography.py**: Hide/reveal messages in images and audio files.
- **P19AdvReverseAt.py & P19AdvReverseVi.py**: Advanced reverse shell with file transfer, logging.
- **P6ScapySniffLocal.py**: Local packet sniffing using scapy.
- **P7ArpSpoofing.py**: ARP spoofing for MITM.
- **P12WifiDeauth.py**: WiFi deauthentication attacks.
- **P17AdvancedArpSpoofing.py**: Combined ARP spoofing and sniffing.

Each module is scriptable and can be run interactively from Banner.py or imported directly in Python code.

---

### Dribs Directory Brute-Forcer

`dribs.py` offers multithreaded brute-forcing of web directories using custom wordlists.

**Workflow:**

1. Enter target URL (default: testphp.vulnweb.com)
2. Select wordlist from local directory
3. Launch up to 100 threads for rapid brute-forcing
4. Results are displayed and colored for easy review

**Code Example:**

```python
from Hacker.dribs import dribsAttack
dribsAttack()
```

---

### Steganography Tools

Hide and reveal messages in images (.png, .bmp) and audio files (.wav) for covert communication or CTF practice.

**Features:**

- Image steganography: Embed and extract messages in pixel LSBs
- Audio steganography: Embed and extract messages in audio frames
- File format checks and error handling

**Code Example:**

```python
from Attacking.P18Steganography import HideData, DecodeI
HideData("input.png", "Secret message", "output.png")
DecodeI("output.png")
```

---

### Reverse Shells

BWhacker includes classic and advanced reverse shells:

- **ReverseAttacker.py / ReverseVictim.py**: Simple shell, command execution.
- **P19AdvReverseAt.py / P19AdvReverseVi.py**: File upload/download, logging, persistent connection.

**Usage:**

1. Run Attacker module on your device, listening on a port.
2. Run Victim module on target, connect back.
3. Send commands, upload/download files, log all interactions.

---

### Web Scraping Automation

`ScrapWeb.py` is a flexible web scraper:

- Downloads HTML content from any URL
- Extracts all URLs containing "https"
- Searches for specific text in web content
- Interactive menu for easy operation

**Code Example:**

```python
from ScrapWeb import ScrapRunner
ScrapRunner()
```

---

### Developer Utilities

- **CppRunner.py**: Run C++ code from Python interface.
- **Tree.py**: Fast file tree search—find files in large directories.
- **Extractor.py**: Extract contents from compressed archive files.

---

### Database & Vulnerable Login

- **Attacking/DataBase.py**: MySQL database connection, table creation for hacking labs.
- **Attacking/VulnLogin.py**: Vulnerable Flask login app for SQL injection practice.

**Example Vulnerable Login:**

```python
@app.route("/login/",methods=["GET","POST"])
def login():
    # SQL injection vulnerable query
    sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cur.execute(sql)
```

---

## Advanced Usage

### Import Modules Directly

All attack and utility scripts can be imported and used programmatically:

```python
from Attacking.P9PasswordGen import PasswordGen
PasswordGen()
```

### Run Banner.py for Interactive CLI

```bash
sudo python3 Hacker/Banner.py
```

---

## Sample Workflows

### Full Attack Chain Example

1. **Reconnaissance**: SubdomainFinder → PortScan → Directory Brute-Force
2. **Web Attacks**: HTTP Fuzzer → SQL Injection → Login Brute-Force
3. **Credential Exploitation**: HashPasswordCrack → PasswordGen
4. **Post-Exploitation**: Reverse Shell Attacker/Victim
5. **Data Exfiltration**: Steganography (Hide in image/audio)

### Example Script

```python
from Attacking.P1PortScan import PortScan
PortScan()
from Attacking.P5BruitForceDirectory import BruiteForceDir
BruiteForceDir()
from Attacking.P13ReverseAttacker import ReverseAttacker
ReverseAttacker()
```

---

## Customization & Extension

- Add your own Python scripts to the `Hacker/Attacking/` directory and import in Banner.py.
- Extend the interactive menu by editing Banner.py and tool_sections.
- Modify wordlist paths, output styles, or logging formats as needed.

---

## Module API Reference

### PortScan

**Function:** PortScan()  
**Description:** Asynchronous port scanner for 20–5000 ports.

### DribsAttack

**Function:** dribsAttack()  
**Description:** Multithreaded brute-forcer; requires wordlist files.

### HideData / DecodeI

**Functions:** HideData(img_path, message, out_path), DecodeI(img_path)  
**Description:** Hide or reveal messages in images.

### PasswordGen

**Function:** PasswordGen()  
**Description:** Generates and rates password strength.

**...** (see source code for full function signatures and usage)

---

## Troubleshooting & FAQ

**Q:** Why do some modules require sudo?
**A:** Network sniffing, ARP spoofing, and deauth attacks need root privileges.

**Q:** MySQL errors?
**A:** Ensure MySQL server is running, credentials are correct, and required Python modules are installed.

**Q:** How do I add custom wordlists?
**A:** Place your wordlist files in the directory specified in dribs.py (`dirbsFile` variable).

**Q:** How to extend the toolkit?
**A:** Add scripts, update Banner.py, and follow the existing module template.

---

## Contributing

- Fork the repo, create a feature branch, submit PRs.
- Report issues in the GitHub Issues section.
- Follow best practices for Python scripting and security research.

---

## License

BSD 3-Clause "New" or "Revised" License.  
See [LICENSE](LICENSE).

---

## Credits

- Project by [abebaw977](https://github.com/abebaw977)
- AbuAll colors by [abu-color](https://pypi.org/project/abu-color/)
- Inspired by open-source hacking tools and CTF labs.

---

## Appendix: Full Menu Example

```
[1] Attacking Tools
    [1] Directory Brute-Force
    [2] Hash Password Crack
    [3] Password Generator
    [4] Login Brute-Force
    [5] SQL Injection
    [6] Reverse Attacker
    [7] Reverse Victim
    [8] Advanced Reverse Attacker
    [9] Advanced Reverse Victim
    [10] Dribs Command
    [11] Password Manager
    [12] Steganography Tool
[2] Sniff Tools
    [1] Local Packet Sniff
    [2] ARP Spoofing
    [3] Wifi Deauthentication
    [4] Advanced ARP Spoofing & Sniffing
[3] Developer Tools
    [1] C++ Runner
    [2] File Search
    [3] Extract File
[4] Web Tools
    [1] Port Scanning
    [2] Subdomain Finder
    [3] HTTP Request Fuzzer
    [4] Web Scraper
    [5] Web Reconnaissance
```

---

## Example Output (PasswordGen)

```text
Enter password length: 12
Enter options (eg, letter=y or n, symbol=..., num=...): y y y
[*] Generated password: aB8@#zLq2!Xv
[*] Password strength: Very strong password
[*] Cracking time: 7.73 years => BlackHacker
```

---

## Example Output (Dribs Directory Brute-Force)

```text
Url : http://testphp.vulnweb.com/
***** [green][bold]admin[bold][/green]
***** [green][bold]images[bold][/green]
Enter file (use above files): admin.txt
[+] Gine Acsess From: http://testphp.vulnweb.com/admin
[X] Not Found: http://testphp.vulnweb.com/backup
...
```

---

## Example Output (Reverse Shell)

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

---

## Example Output (Steganography)

```text
[*] Message hidden in image: output.png
[**] Hidden MSG: This is a secret!
```

---

## Example Output (Web Scraper)

```text
Enter URL: https://example.com
[*] Found 42 links containing 'https'
[*] Search for: 'login'
[*] Found: login page at /login
```

---

## Final Notes

For latest updates, advanced workflows, and full code reference, see [BWhacker on GitHub](https://github.com/abebaw977/BWhacker).  
You are encouraged to explore, extend, and contribute to this beastly toolkit!

---
