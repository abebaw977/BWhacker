import aiohttp
import asyncio
import math

with open("SubD.txt", "r") as f:
    subs = [line.strip() for line in f if line.strip()]

CONCURRENCY = 5
semaphore = asyncio.Semaphore(CONCURRENCY)
results = []
counter = 0
lock = asyncio.Lock()

async def check_subdomain(session, sub, total):
    global counter
    url = f"https://{sub}.google.com"

    async with semaphore:
        try:
            async with session.get(url, timeout=1) as resp:
                status = resp.status
                async with lock:
                    counter += 1
                    pct = math.floor((counter / total) * 100)
                    if status in (200, 302, 403, 503):
                        print(f"[*] success => {status} {url}")
                        results.append(url)
                    else:
                        print(f"[-] failed  => {status} {url}")
                    print(f"Progress: {pct}%   ", end="\r", flush=True)
        except Exception as e:
            async with lock:
                counter += 1
                pct = math.floor((counter / total) * 100)
                print(f"[!] {url} Error => {type(e).__name__}: {e}")
                print(f"Progress: {pct}%   ", end="\r", flush=True)

async def main():
    total = len(subs)
    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    timeout = aiohttp.ClientTimeout(total=3)
   
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        tasks = [check_subdomain(session, s, total) for s in subs]
        await asyncio.gather(*tasks)
    if results:
        with open("SubDomain.txt", "a") as out:
            out.write("\n".join(results) + "\n")
    print()

if __name__ == "__main__":
    asyncio.run(main())
