import os
import subprocess
from abu_color import AbuAll



def CppDev():
    file = input(AbuAll("\nFile Name: ",sty="b"))
    outs = input(AbuAll("File Out Binary: ",sty="b"))

    FilePath=os.getcwd()
    print(FilePath)
    result=subprocess.check_output("ls",shell=True).decode().split("\n")
    outputs=""
    while True:
        print(AbuAll("\n"+"="*45,bg="green"))
        systems = input(AbuAll(f"===> {" "*9}Exit q,continue ... :- ",bg="yellow",sty="b"))
        print(AbuAll("="*45,bg="green"))
        if systems == "q":
            break
        if systems in ["c","clear"]:
            subprocess.run(f"clear",shell=True)
        try:
            os.system(f"g++ {file} -o {outs}")
            #subprocess.Popen("clear;g++ {} -o {};".format(file,outs,outs),shell=True)
            os.system(f"./{outs}")
        except Exception as e:
            print("Error: ",e)
#print(outputs)
