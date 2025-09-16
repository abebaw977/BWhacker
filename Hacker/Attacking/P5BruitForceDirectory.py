import asyncio
import aiohttp
import os
from tqdm.asyncio import tqdm_asyncio
fast = asyncio.Semaphore(1000)
async def BruitForce(url,files):
    Dir=[]
    try:
        with open(files,"r") as f:
            Dir=[l.strip() for l in f if l.strip()]
    except:
        print("File Not Found")
        return
    async with aiohttp.ClientSession() as ses:
        Req=[requests(ses,url,dirs) for dirs in Dir]
        await tqdm_asyncio.gather(*Req)
    print("Result is saved on 5-result.txt")
async def requests(ses,url,dirs):
    async with fast:
        try:
            async with ses.get(url + "/" + dirs) as res:
                if res.status in [200, 302]:
                    with open("5-result.txt","a") as r:
                        r.write(f"[*] Found Url => {res.url} {res.status} \n")
        except Exception as e:
            print(f"[!] {e}")
async def Main():
    url = input("Enter target url: ").strip()
    files = input("Enter Directory file: ").strip()
    if not url or not files:
        print("Please fill all request !!")
        return
    try:
        os.system("rm 5-result.txt")
    except:
        pass
    await BruitForce(url,files)
def BruiteForceDir():
    asyncio.run(Main())
