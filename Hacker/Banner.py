from abu_color import AbuAll

def banner():
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    print(AbuAll(f"##{" "*20} BWAbuHacker{" "*20}   ###",bg="blue",sty="b"))
    for i in range(2):
        print(AbuAll("*"*60,bg="blue"))
    choice = ["DNS Resolve","Dribs Command","XXS Attacking"]
    for index,ch in enumerate(choice):
        print(AbuAll(f"{str(index+1)+"."} {ch}",bg="red",sty="b"))
def command():
    while True:
        try:
            comand=int(input("Enter choice by index: "))
            match (comand):
                case (1):
                    import dribs
                case (2):
                    print("Try")
                case 0:
                    break
                case _:
                    print("Invalid Value")
        except ValueError:
            print("Enter only number,try again")
    # end match
if __name__ == "__main__": 
    print("yes")
    banner()
    command()
    #dirbs()