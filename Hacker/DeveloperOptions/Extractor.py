import os
import subprocess
import zipfile
from abu_color import AbuAll
paths=os.getcwd()

help="""
Commands:
    cd <path>       Change the current working directory.
    xf <file.zip>   Extract only files matching a user-specified extension
                    (e.g., .mp4, .py) from the given ZIP archive.
    ls              List files and folders in the current directory.
                    Directories are shown in blue; files in white.
    exit            Exit the shell.
    help            help banner

Notes:
    - ZIP extraction will prompt you for the file extension you want.
    - Paths can be absolute or relative.
    - Only basic shell-like commands are supported in this interface.
    - Colored output is provided by the abu_color.AbuAll function.
"""
def extract_spec(file):
    if not os.path.isfile(file):
        print("file not found")
        return
    if not zipfile.is_zipfile(file):
        print("Invalid zip file")
        return
    ES=input("Enter Specifi extractor(.mp4,or ,py,etc): ").strip()
    with zipfile.ZipFile(file,"r") as ZE:
        for Ze in ZE.namelist():
            if Ze.endswith(ES):
                ZE.extract(Ze,paths)
                print(f"File Extracetd ({Ze})")
            else:
                print(f"Not Found File ({ES})")
def SubProcess(thing):
    try:
        result=subprocess.Popen(f"{thing}",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        return result.stdout.read()+result.stderr.read()
    except Exception as e:
        print(AbuAll(e,bg="bred"))
def extractor_file():
    print(help)
    while True:
        global paths
        cmd=input(AbuAll(f"(extract){paths}:: ",bg="yellow",sty="b"))
        if "cd" in cmd:
            if cmd.startswith("cd "):
                target_path=cmd[3:].strip()
                try:
                    os.chdir(target_path)
                    paths=os.getcwd()
                except FileNotFoundError:
                    print("File Not Found")
        elif cmd.startswith("xf "):
            extract_spec(cmd[3:].strip())
        elif "ls" in cmd:
            value=SubProcess(cmd)
            for v in value.splitlines():
                if os.path.isdir(v):
                    print(AbuAll(v.decode(),bg="blue",sty="b"))
                if not os.path.isdir(v):
                    print(AbuAll(v.decode(),bg="white"))
        elif "exit" in cmd:
            break
        elif "help" in cmd:
            print(help)
        elif cmd == "":
            continue
        else:
            print("This shell only support zip ,ls,exit and cd Command !!")
