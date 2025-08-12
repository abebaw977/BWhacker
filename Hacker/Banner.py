from abu_color import AbuAll
from xss import XssAttack
from dribs import dribsAttack
from DnsResolve import subdomain_bruteforce

def banner():
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    print(AbuAll(f"##{" "*20} BWAbuHacker{" "*20}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    choice = ["DNS Resolve","Dribs Command","XXS Attacking","Developer Options","to Exit enter 0"]
    for index,ch in enumerate(choice):
        print(AbuAll(f"{str(index+1)+"."} {ch}",bg="red",sty="b"))
def DeveloperOptions():
    return "Try"
def command():
    while True:
        try:
            comand=int(input(AbuAll("Enter choice by index: ",bg="yellow",sty="b")))
            match (comand):
                case (1):
                   subdomain_bruteforce() 
                case (2):
                    dribsAttack()
                case 3:
                    XssAttack()
                case 4:
                    print(DeveloperOptions())
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