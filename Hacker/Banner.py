import os
import subprocess
from abu_color import AbuAll
from Attacking.P1PortScan import PortScan
from Attacking.P2SubDomainFinder import SubDomain
from Attacking.P3Keylogger import Run
from Attacking.P4HttpFuzzer import HttpFuzzer
from Attacking.P5BruitForceDirectory import BruiteForceDir
from Attacking.P6ScapySniffLocal import ScapySniff
from Attacking.P7ArpSpoofing import ArpSpoof
from Attacking.P8HashPasswordCrack import HashPassC
from Attacking.P9PasswordGen import PasswordGen
from Attacking.P11BruiteForceLogin import BrutForceLogin
from Attacking.P12WifiDeauth import WifiDeauth
from Attacking.P14SqlInjection import SqlAtcking
from Attacking.P13ReverseAttacker import ReverseAttacker
from Attacking.P13ReverseVictim import RreverseVictim
from Attacking.P16PasswordManager import PasswordManagers
from Attacking.P17AdvancedArpSpoofing import ArpSpoofAndSnoffing
from Attacking.P18Steganography import SryphtoSecretData
from dribs import dribsAttack
from DeveloperOptions.Tree import TreeSearch
from DeveloperOptions.CppRunner import CppDev
from DeveloperOptions.Extractor import extractor_file
from ScrapWeb import ScrapRunner

def webRecon():
    try:
        result = subprocess.run(
            ["bash", "./Attacking/P10WebRecon.sh"],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"[!] Error running script: {e}")
def banner():
    os.system("clear")
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    print(AbuAll(f"##{" "*20} BWAbuHacker{" "*20}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    choice = [
        "Port scaninng",
        "SubDomain Finder",
        "Http request Fuzzer",
        "Beast Hacking password Gen",
        "Cracking hash password",
        "Dribs Command",
        "Key Logger",
        "Developer Options",
        "SQl injection for login page",
        "Scrap web",
        "Web reconnaissance by bash",
        "BruitForce for web directory",
        "BruitForce for login page",
        "Sniff loacl packet",
        "Arp spoofing ",
        "Wifi Deauthenticaion",
        "Advance ARP spoofing and sniffing"
        "Reverse Hacking Attacker<=>Victim Two file",
        "Password Manager",
        "Steganography Tool to hide data on image or audio"
        "to Exit enter 0"
        ]
    for index,ch in enumerate(choice):
        print(AbuAll(f"{str(index+1)+"."} {ch}",bg="red",sty="b"))
def DeveloperOptions():
    os.system("clear")
    for i in range(2):
        print(AbuAll("="*60,bg="blue"))
    print(AbuAll(f"##{" "*12}Wellcom To developer options{" "*12}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("="*60,bg="blue"))
    choice = [
        "Beast C++ runner",
        "Beast File search",
        "Extract file",
        "to Exit enter 0"
        ]
    for index,ch in enumerate(choice):
        print(AbuAll(f"{str(index+1)+"."} {ch}",bg="red",sty="b"))
    while True:
        try:
            comand=int(input(AbuAll("(dev)Enter choice by index: ",bg="yellow",sty="b")))
            match (comand):
                case 1:
                   CppDev()
                case 2:
                   TreeSearch()
                case 3:
                    extractor_file()
                case 0:
                    break
                case _:
                    print("Invalid Value")
        except ValueError:
            print(AbuAll("Enter only number,try again",bg="yellow",sty="b"))
def command():
    while True:
        try:
            comand=int(input(AbuAll("(Home)Enter choice by index: ",bg="yellow",sty="b")))
            match (comand):
                case 1:
                    PortScan()
                case 2:
                   SubDomain() 
                case 3:
                    HttpFuzzer()
                case 4:
                    PasswordGen()
                case 5:
                    HashPassC()
                case 6:
                    dribsAttack()
                case 7:
                    Run()
                case 8:
                    DeveloperOptions()  
                case 9:
                    SqlAtcking()
                case 10:
                    ScrapRunner()
                case 11:
                    webRecon()
                case 12:
                    BruiteForceDir()
                case 13:
                    BrutForceLogin()
                case 14:
                    ScapySniff()
                case 15:
                    ArpSpoof()
                case 16:
                    WifiDeauth()
                case 17:
                    ArpSpoofAndSnoffing()
                case 18:
                    print("""
    ReverseAttacker => Listens for a connection, sends commands, 
            and can download files from the connected host.
    reverseVictim => Connects back to the attacker, runs received 
            commands, or sends file contents.
        useage:
            Run ReverseAttacker on your device to listen => then 
            run ReverseVictim on the target device to connect back 
            and exchange commands/files  
                    """)
                case 19:
                    PasswordManagers
                case 20:
                    SryphtoSecretData()
                case 0:
                    break
                case _:
                    print("Invalid Value")
        except ValueError:
            print(AbuAll("Enter only number,try again",bg="yellow",sty="b"))
if __name__ == "__main__": 
    banner()
    command()