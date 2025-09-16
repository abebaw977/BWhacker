import os
from abu_color import AbuAll
from xss import XssAttack
from dribs import dribsAttack
from DnsResolve import subdomain_bruteforce
from DeveloperOptions.Tree import TreeSearch
from DeveloperOptions.CppRunner import CppDev
from DeveloperOptions.Extractor import extractor_file
from ScrapWeb import ScrapRunner
def banner():
    os.system("clear")
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    print(AbuAll(f"##{" "*20} BWAbuHacker{" "*20}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    choice = ["DNS Resolve","Dribs Command","XXS Attacking","Developer Options","Scrap web","to Exit enter 0"]
    for index,ch in enumerate(choice):
        print(AbuAll(f"{str(index+1)+"."} {ch}",bg="red",sty="b"))
def DeveloperOptions():
    os.system("clear")
    for i in range(2):
        print(AbuAll("="*60,bg="blue"))
    print(AbuAll(f"##{" "*12}Wellcom To developer options{" "*12}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("="*60,bg="blue"))
    choice = ["Beast C++ runner","Beast File search","Extract file","to Exit enter 0"]
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
                   subdomain_bruteforce() 
                case 2:
                    dribsAttack()
                case 3:
                    XssAttack()
                case 4:
                    DeveloperOptions()
                case 5:
                    ScrapRunner()
                case 0:
                    break
                case _:
                    print("Invalid Value")
        except ValueError:
            print(AbuAll("Enter only number,try again",bg="yellow",sty="b"))
    # end match
if __name__ == "__main__": 
    banner()
    command()