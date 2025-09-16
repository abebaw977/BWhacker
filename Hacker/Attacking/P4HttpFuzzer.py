import asyncio
import aiohttp
from tqdm.asyncio import tqdm_asyncio
fast = asyncio.Semaphore(100)

async def Fuzzer(url,method,files,param):
    payloads=[]
    names=[]
    method = method.upper()
    try:
        if isinstance(files,list):
            with open(files[0],"r") as py:
                payloads=[line.strip() for line in py if line.strip()]
            with open(files[1],"r") as na:
                names=[name.strip() for name in na if name.strip()]
        else:
            with open(files,"r") as py:
                payloads=[line.strip() for line in py if line.strip()] 
    except Exception as e:
        print(e)
        return
    timeout = aiohttp.ClientTimeout(total=25)
    async with aiohttp.ClientSession(timeout=timeout) as request:
        if isinstance(files,list):
            task=[send_r(request,url,method,payload,param,NA) 
                for payload in payloads for NA in names 
            ]
        else:
            task=[send_r(request, url, method, payload, param) for payload in payloads]
        await tqdm_asyncio.gather(*task)
async def send_r(request,url,method,payload,param,NA=None):
    async with fast:
        try:
            if method == "GET":
                res = await request.get(url,params={param:payload})
            elif method == "POST":
                if isinstance(param,list):
                    PAYLOAD={
                        param[0]:NA,
                        param[1]:payload
                        }
                    res = await request.post(url,data=PAYLOAD)
                else:
                    res = await request.post(url,data={param:payload})
            else:
                print("[!] unsupported methods.")
                return

            if res.status in [200,302]:
                text = await res.text()
                if isinstance(param,list):
                    if "wellcome" in text.lower() or "logout" in text.lower():
                        with open("result.txt","a") as r:
                            r.write(f"Valid => {NA}:{payload}\n")
                            return        
                else:
                    with open("result.txt","a") as r:
                        snippet = text[:200].replace("\n", " ")
                        r.write(f"[{res.status}] {payload} -> {snippet}\n")
        except aiohttp.ClientError as e:
            print(f"[!] Error with payload '{payload}': {e}",end="\r")
def choice():
    print("""
    Choice
       1 .sample => 1 param
       2 .login => 2 param
    """)
async def main():
    global param
    url = input("Enter url (http://example.com): ")
    method = input("Enter method (POST\\get): ")
    choice()
    l= int(input("Enter length of parameters: ").strip())

    if l==2:
        firstP=input("(param)Enter first Parm: ")
        secondP=input("(param)Enter second Parm: ")
        file1=input("(file)Enter payload (Pass..): ")
        file2=input("(file)Enter payload (Name..): ")
        param=[firstP,secondP]
        files=[file1,file2]
    elif l==1:
        param=input("(param)Enter payload for (param Url): ")
        files=input("(file)Enter params: ")
    else:
        print("Only support 1 or 2")
        return

    await Fuzzer(url,method,files,param)
def HttpFuzzer():
    asyncio.run(main())
