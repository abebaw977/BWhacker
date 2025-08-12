# BWhacker

> **BWhacker** — a collection of Python utilities for security learning and testing.  
> Use only on systems you own or have explicit written permission to test.

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

# Repository layout

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/abebaw977/BWhacker.git
   cd BWhacker
