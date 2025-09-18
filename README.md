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

# Project overview

`BWhacker` collects small, focused scripts that demonstrate common reconnaissance and simple injection testing techniques:
- DNS subdomain discovery
- Directory brute-force (wordlist scanning)
- Sending payloads via POST to check basic injection indicators
- An interactive banner/launcher that ties these tools together

**Intended use:** learning, authorized penetration testing, or lab exercises only.

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
