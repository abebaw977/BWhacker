![Description](https://github.com/abebaw977/BWhacker/blob/main/Screenshot_20250815_161616_UserLAnd.jpg)
# BWhacker

> **BWhacker** — a collection of Python utilities for security learning and testing.

---

# Table of contents

1. [Project overview](#project-overview)  
2. [Repository layout](#repository-layout)  
3. [Requirements & installation](#requirements--installation)  
4. [Quick start — run the interactive launcher](#quick-start---run-the-interactive-launcher)  
5. [Module reference and deep usage examples (with terminal output samples)](#module-reference-and-deep-usage-examples-with-terminal-output-samples)  
   - [DnsResolve — subdomain brute-force](#dnsresolve---subdomain-brute-force)  
   - [dribs — dirb-like directory scan](#dribs---dirb-like-directory-scan)  
   - [xss — payload POST testing](#xss---payload-post-testing)  
   - [Banner — interactive launcher and menu](#banner---interactive-launcher-and-menu)  
6. [Wordlists & example files](#wordlists--example-files)  
7. [Troubleshooting & common errors](#troubleshooting--common-errors)  
8. [Security, ethics & legal](#security-ethics--legal)  
9. [Development & contributing guide](#development--contributing-guide)  
10. [FAQ](#faq)  
11. [Changelog, credits & license](#changelog-credits--license)

---

# BWhacker Hacker Module Overview

The Hacker folder in the BWhacker repository is a collection of small security and penetration-testing scripts, organized into functional categories. This module provides tools for network scanning, web reconnaissance, password testing, system exploitation, and developer utilities.

## Folder Structure & Description
## 2. Banner.py
  # Banner.py Overview

`Banner.py` is the **main interactive launcher** for the `BWhacker` project.  
It provides a **menu-driven interface** to run various hacking, penetration testing, and developer utility scripts in the repository.

---

## Key Features

1. **Interactive Menus**
   - `banner()` — Displays the main menu with options for:
     - Port scanning, subdomain enumeration, HTTP fuzzing
     - Password generation & hash cracking
     - Directory brute-force, login brute-force
     - Web scraping, SQL injection testing
     - Reverse shell attacker/victim
     - Developer options
   - `DeveloperOptions()` — Sub-menu for:
     - C++ runner
     - File search (`TreeSearch`)
     - File extraction (`extractor_file`)

2. **Integration with Scripts**
   - Imports functions from:
     - `Attacking/` scripts: `PortScan`, `SubDomain`, `HttpFuzzer`, `BruiteForceDir`, etc.
     - `dribs.py` → `dribsAttack`
     - `DeveloperOptions/` → `CppDev`, `TreeSearch`, `extractor_file`
     - `ScrapWeb.py` → `ScrapRunner`
   - Executes Bash scripts (`P10WebRecon.sh`) using `subprocess`.

3. **User Input Handling**
   - Accepts numeric choices and matches them with corresponding tool functions.
   - Handles invalid inputs with clear warnings.

4. **Visual Enhancements**
   - Uses `AbuAll` (from `abu_color`) for styled colored terminal output.
   - ASCII decorations to separate menus visually.

5. **Exit / Looping**
   - Both main menu and developer options menu loop until the user selects `0` to exit.

---

## Workflow

1. Run `Banner.py`:
```bash
      sudo python3 Banner.py
```
## 2. Attacking/
- Contains the main offensive and testing scripts

  **P15AdvanceRecon.sh**	Sequentially numbered scripts for recon, scanning, fuzzing, and ePort scanning, HTTP fuzzing, Directory brute-force, web scraping, etc.)
  
  **VulnLogin.py** 	Vulnerable login page demo (for lab/testing purposes)

  **SubD.txt, SubDomain.txt, ethiopia.txt**	Example input/wordlist files used by scripts

  **templates/**	HTML templates for web-based demos (DashB.html, VulnLogin.html)


</div>

---

## Repository layout
```
BWhacker/
├── books/
│   └── hack/
├── Hacker/
│   ├── BackDoor/
│   │   ├── backdoor.py
│   │   └── servers.py
│   ├── Banner.py
│   ├── BlackHat.py
│   ├── DnsResolve.py
│   ├── First.py
│   ├── dnscan/
│   │   ├── Dockerfile
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── dnscan.py
│   │   ├── requirements.txt
│   │   ├── subdomains-100.txt
│   │   ├── subdomains-1000.txt
│   │   ├── subdomains-10000.txt
│   │   ├── subdomains-500.txt
│   │   ├── subdomains-uk-1000.txt
│   │   ├── subdomains-uk-500.txt
│   │   ├── subdomains.txt
│   │   ├── suffixes.txt
│   │   └── tlds.txt
│   ├── dribs.py
│   └── xss.py
├── LICENSE
├── README.md
└── requirements.txt
```
## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/abebaw977/BWhacker.git
   cd BWhacker
---

# Requirements & installation

Minimum environment:
- Linux-like environment (UserLAnd, Termux, Ubuntu, etc.)
- Python 3.8+ recommended
- pip3

## Install system packages (example for Debian/Ubuntu / UserLAnd)
```bash
sudo apt update && sudo apt install -y python3 python3-pip git
```
# Install Python dependencies
Install:
```bash
pip3 install -r requirements.txt
```
## Quick start — run the interactive launcher

From repo root:
```bash
python3 Hacker/Banner.py
```
Example session (simulated):

$ python3 Hacker/Banner.py
```
************************************************************
************************************************************
##                     BWAbuHacker                        ###
************************************************************
************************************************************
1. DNS Resolve
2. Dribs Command
3. XXS Attacking
4. Developer Options
5. to Exit enter 0

Enter choice by index: 1
 Enter target domain (e.g., example.com): testphp.vulnweb.com
 Enter path to wordlist (e.g., subdomains.txt): ./wordlists/subdomains.txt
🔍 Starting brute-force on: testphp.vulnweb.com
[FOUND] www.testphp.vulnweb.com --> 54.86.44.34
[FOUND] admin.testphp.vulnweb.com --> 54.86.44.34
Enter choice by index:
```
