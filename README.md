![Description](https://github.com/abebaw977/BWhacker/Bwhacker/Screenshot_20250815_161616_UserLAnd.jpg)
# BWhacker

> **BWhacker** — a collection of Python utilities for security learning and testing.

---
## Table of Contents
1. [Installation](#installation)
2. [Requirements & Setup](#requirements--setup)
3. [Tools Overview](#tools-overview)
    - [Banner.py](#bannerpy)
    - [ScrapWeb.py](#scrapwebpy)
    - [dribs.py](#dribspy)
    - [Attacking/](#attacking)
4. [Usage](#usage)
5. [Developer Options](#developer-options)
6. [Security & Ethics](#security--ethics)
7. [Contributing](#contributing)
8. [License](#license)

---

# BWhacker Hacker Module Overview

The Hacker folder in the BWhacker repository is a collection of small security and penetration-testing scripts, organized into functional categories. This module provides tools for network scanning, web reconnaissance, password testing, system exploitation, and developer utilities.

## Folder Structure & Description






## 1. Banner.py
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

6. **Run Banner.py**:

```bash
      sudo python3 Banner.py
```
   - 	Why sudo,It have scapy python modules



## 2. ScrapWeb.py

`ScrapWeb.py` is a **simple web scraping utility** in the BWhacker project that allows you to:

- Download the HTML content of a website.
- Extract URLs containing "https".
- Search for specific text strings in the page content.
- Run in an interactive, menu-driven interface.


## Key Functions

1. **download_file()**
   - Prompts the user to enter a URL.
   - Downloads the HTML content and saves it as `index.html`.
   - Handles exceptions for invalid URLs or connection errors.

2. **UrlScrap(SearchScrap)**
   - Calls `download_file()` to fetch the page.
   - Scans the downloaded HTML for URLs containing `SearchScrap` (usually `"https"`).
   - Prints each found URL with a count of results.
   - Handles file not found and general errors.

3. **textScrap()**
   - Calls `download_file()` to fetch the page.
   - Prompts the user to enter a search string.
   - Scans the HTML file line by line for the text.
   - Prints all occurrences along with the line index.
   - Notifies if the text is not found.

4. **ScrapRunner()**
   - Interactive menu to choose between:
     1. URL scraping
     2. Text scraping
     3. Exit
   - Loops until the user chooses to exit.
   - Calls `UrlScrap()` or `textScrap()` based on user input.


## 3. dribs.py


`dribs.py` is a **directory brute-force scanner**. It attempts to discover valid paths on a target website using predefined wordlists.


## Features

- Accepts a target URL (defaults to `http://testphp.vulnweb.com/`).
- Loads wordlists from a configurable directory.
- Uses **multithreading** (`ThreadPoolExecutor`) for faster scanning.
- Prints found URLs, redirects, and server errors using **rich** for colored output.



## 4. Attacking/
- Contains the main offensive and testing scripts

  1. **P15AdvanceRecon.sh**	Sequentially numbered scripts for recon, scanning, fuzzing, and ePort scanning, HTTP fuzzing, Directory brute-force, web scraping, etc.)
  
  2. **VulnLogin.py** 	Vulnerable login page demo (for lab/testing purposes)

  3. **SubD.txt, SubDomain.txt, ethiopia.txt**	Example input/wordlist files used by scripts

  4. **templates/**	HTML templates for web-based demos (DashB.html, VulnLogin.html)




## 5. DeveloperOptions/

Utilities aimed at developers or automation:

- File	Description

  1. **CppRunner.py**	Run or compile C++ code from Python

  2. **Extractor.py**	Extract files or data from zip by choice mp4,py,php etc /outputs
  3. **Tree.py**	Display file structures, directories, or tree views

---





## Repository layout
```
|-- BWhacker
|   |-- Hacker
|   |   |-- Attacking
|   |   |   |-- DataBase.py
|   |   |   |-- Database.php
|   |   |   |-- Login.py
|   |   |   |-- P10WebRecon.sh
|   |   |   |-- P11BruiteForceLogin.py
|   |   |   |-- P12WifiDeauth.py
|   |   |   |-- P13ReverseAttacker.py
|   |   |   |-- P13ReverseVictim.py
|   |   |   |-- P14SqlInjection.py
|   |   |   |-- P15AdvanceRecon.sh
|   |   |   |-- P17PasswordManager.py
|   |   |   |-- P1PortScan.py
|   |   |   |-- P2SubDomainFinder.py
|   |   |   |-- P3Keylogger.py
|   |   |   |-- P4HttpFuzzer.py
|   |   |   |-- P5BruitForceDirectory.py
|   |   |   |-- P6ScapySniffLocal.py
|   |   |   |-- P7ArpSpoofing.py
|   |   |   |-- P8HashPasswordCrack.py
|   |   |   |-- P9PasswordGen.py
|   |   |   |-- SubD.txt
|   |   |   |-- SubDomain.txt
|   |   |   |-- VulnLogin.py
|   |   |   |-- ethiopia.txt
|   |   |   `-- templates
|   |   |       |-- DashB.html
|   |   |       `-- VulnLogin.html
|   |   |-- Banner.py
|   |   |-- BlackHat.py
|   |   |-- DeveloperOptions
|   |   |   |-- CppRunner.py
|   |   |   |-- Extractor.py
|   |   |   `-- Tree.py
|   |   |-- DnsScan
|   |   |   |-- requirements.txt
|   |   |   |-- subdomains-100.txt
|   |   |   |-- subdomains-1000.txt
|   |   |   |-- subdomains-10000.txt
|   |   |   |-- subdomains-500.txt
|   |   |   |-- subdomains-uk-1000.txt
|   |   |   |-- subdomains-uk-500.txt
|   |   |   |-- subdomains.txt
|   |   |   |-- suffixes.txt
|   |   |   `-- tlds.txt
|   |   |-- ScrapWeb.py
|   |   |-- SubD.txt
|   |   |-- dribs.py
|   |   `-- index.html
|   |-- LICENSE
|   |-- README.md
|   |-- Screenshot_20250916_145958_UserLAnd.jpg
|   `-- requirement.txt
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
