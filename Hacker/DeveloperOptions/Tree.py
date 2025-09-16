import os
import sys

def TreeSearch():
    def tree(path,pre=""):
        FileR=[]
        paths=os.getcwd()
    
        for i,file in enumerate(os.listdir(path)):
            Path=os.path.join(path,file)
            con="■■"
            FileR.append(file)
            print(pre+con,file)
            if os.path.isdir(Path):
                ext="   "
                tree(Path,ext+pre)
                FileR.append(Path)
        def search():
            if len(sys.argv)>1:
                #This use of ls file if not use arguments 
                if len(sys.argv) != 3:
                    print(" Invalid Value\n Usage: python3 Tree.py -s [FileName]")
                    sys.exit()
            if len(sys.argv) == 3:
                options = sys.argv[1]
                SearchFile=sys.argv[2]
                if os.path.isdir(SearchFile):
                    FoundFolder=os.path.join(os.getcwd(),SearchFile)
                    print(f"Found: {SearchFile}")
                    print(f"Folder Path: {FoundFolder}")
                elif options.strip() == "-s":
                    if SearchFile in FileR:
                        print(f"Found: {SearchFile}")
                        sys.exit()
                else:
                    print("invalid options, Try again")
                    sys.exit()
                if SearchFile not in FileR:
                    print("File Not Found")
        search()
    tree("./")
