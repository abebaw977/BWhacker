import os
import subprocess
from abu_color import AbuAll
from Attacking.P1PortScan import PortScan
from Attacking.P2SubDomainFinder import SubDomain
from Attacking.P4HttpFuzzer import HttpFuzzer
from Attacking.P5BruitForceDirectory import BruiteForceDir
from Attacking.P8HashPasswordCrack import HashPassC             from Attacking.P9PasswordGen import PasswordGen
from Attacking.P11BruiteForceLogin import BrutForceLogin
from Attacking.P14SqlInjection import SqlAtcking                from Attacking.P13ReverseAttacker import ReverseAttacker
from Attacking.P13ReverseVictim import RreverseVictim
from Attacking.P16PasswordManager import PasswordManagers
from Attacking.P18Steganography import SryphtoSecretData        from Attacking.P19AdvReverseAt import ReverseAttacker as AdvReverseAttacker
from Attacking.P19AdvReverseVi import ReverseV
from dribs import dribsAttack                                   from DeveloperOptions.Tree import TreeSearch
from DeveloperOptions.CppRunner import CppDev
from DeveloperOptions.Extractor import extractor_file
from ScrapWeb import ScrapRunner
from Attacking.P6ScapySniffLocal import ScapySniff              from Attacking.P7ArpSpoofing import ArpSpoof
from Attacking.P12WifiDeauth import WifiDeauth
from Attacking.P17AdvancedArpSpoofing import ArpSpoofAndSnoffing

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

tool_sections = [
    {
        "header": "*** Attacking Tools",
        "choices": [
            ("BruitForce for web directory", BruiteForceDir),
            ("Cracking hash password", HashPassC),
            ("Beast Hacking password Gen", PasswordGen),
            ("BruitForce for login page", BrutForceLogin),
            ("SQl injection for login page", SqlAtcking),
            ("Reverse Hacking Attacker", ReverseAttacker),
            ("Reverse Hacking Victim", RreverseVictim),
            ("Advanced Reverse Attacker", AdvReverseAttacker),
            ("Advanced Reverse Victim", ReverseV),
            ("Dribs Command", dribsAttack),
            ("Password Manager", PasswordManagers),
            ("Steganography Tool to hide data on image or audio", SryphtoSecretData),
        ]
    },
    {
        "header": "*** Sniff Tools",
        "choices": [
            ("Sniff local packet", ""),
            ("Arp spoofing", "ArpSpoof"),
            ("Wifi Deauthentication", "WifiDeauth"),
            ("Advance ARP spoofing and sniffing", "ArpSpoofAndSnoffing"),
        ]
    },
    {
        "header": "*** Developer Tools",
        "choices": [
            ("Beast C++ runner", CppDev),
            ("Beast File search", TreeSearch),
            ("Extract file", extractor_file)
        ]
    },
    {
        "header": "*** Web Tools",
        "choices": [
            ("Port scaninng", PortScan),
            ("SubDomain Finder", SubDomain),
            ("Http request Fuzzer", HttpFuzzer),
            ("Scrap web", ScrapRunner),
            ("Web reconnaissance by bash", webRecon)
        ]
    },
    {
        "header": "*** Other",
        "choices": [
            ("to Exit enter 0", None)
        ]
    }
]

def banner():
    os.system("clear")
    border = AbuAll("#" * 60, bg="blue")
    inb = AbuAll("*" *4,bg="red",sty="b")
    print(border)
    print(border)
    print(AbuAll(f"{' '*20}{inb} BWAbuHacker {inb}{' '*20}", bg="blue", sty="b"))
    print(border)
    print(border)
    idx = 1
    for section in tool_sections:
        print(AbuAll(section["header"], bg="green", sty="b"))
        for label, _ in section["choices"]:
            if label.lower().startswith("to exit"):
                print(AbuAll(f"    0. {label}", bg="red", sty="b"))
            else:
                print(AbuAll(f"    {idx}. {label}", bg="red", sty="b"))
                idx += 1

def get_choice_function(choice_index):
    idx = 1
    for section in tool_sections:
        for label, func in section["choices"]:
            if label.lower().startswith("to exit") and choice_index == 0:
                return None
            if not label.lower().startswith("to exit"):
                if idx == choice_index:
                    return func
                idx += 1
    return None

def command():
    while True:
        try:
            user_input = input(AbuAll("(Home)Enter choice by index: ", bg="yellow", sty="b"))
            comand = int(user_input)
            if comand == 0:
                break
            func = get_choice_function(comand)
            if func:
                func()
            else:
                print(AbuAll("Invalid Value", bg="yellow", sty="b"))
        except ValueError:
            print(AbuAll("Enter only number, try again", bg="yellow", sty="b"))

if __name__ == "__main__":
    banner()
    command()
