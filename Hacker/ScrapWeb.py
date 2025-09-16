import requests
from abu_color import AbuAll
import sys
print(AbuAll("Hi abuman",bg="red"))

def download_file():
    UrlUser=input(AbuAll("Enter url: ",bg="blue",sty="b"))
    try:
        r = requests.get(UrlUser)
        with open("index.html","w") as f:
            f.write(r.text)
    except Exception as e:
        print("Error: ",e)
    except FileNotFoundError:
        print("Please Check Url or connection")

def UrlScrap(SearchScrap):
    download_file()
    try:
        f = open("index.html","r")
        counts=0
        for fs in f:
            for lists in fs.split():
                    if SearchScrap in lists:
                        Files = lists.split("https://")
                        #print(Files)
                        for p in Files[1:]:
                            url = "https://"+p.split("'")[0].split(">")[0].split("\"")[0]
                            print(AbuAll("Found Url: ",bg="yellow",sty="b"),AbuAll(url,bg="green",sty=['u','b']))
                            counts+=1
                    #print("yes")
        print(AbuAll(f"Found Results: {AbuAll(str(counts),bg="red")}",fg="byellow",bg="black",sty="b"))
    except FileNotFoundError as e:
        print(AbuAll("File Not found: ",bg="red"),e)
    except Exception as e:
        print("Something errors: ",e)
def textScrap():
    download_file()
    bo=True
    f=open("index.html","r")
    searched=input(AbuAll("Enter searching text (any text) : ",bg="yellow",sty="b"))
    try:
        for index, Searching in enumerate(f):
            for search in Searching.split():
                if searched in search:
                    print(AbuAll("Found at ",bg = "yellow")+(f"{index} : {search}"))
                    bo=False
        if bo:
            print(AbuAll(f"Not found: {searched}",bg="bred"))
    except Exception as e:
        print("Error: ",e)

def ScrapRunner():
    for i,l in enumerate(["Url scraps","Text scrap","to exit enter 0"]):
        print(AbuAll(f"{str(i+1)+"."} {l}",bg="red",sty="b"))
    while True:
        c=input(AbuAll("(scrap)Enter index: ",bg="yellow",sty="b"))
        if c == "1":
            UrlScrap("https")
        elif c == "2":
            textScrap()
        elif c =="0":
            break
        else:
            print("Invalid value")
