import socket
import asyncio
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
COMMON_PORTS = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP (Submission)",
    636: "LDAPS",
    873: "Rsync",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "MSSQL",
    1521: "Oracle DB",
    2049: "NFS",
    2082: "cPanel",
    2083: "cPanel SSL",
    2181: "Zookeeper",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion (SVN)",
    4444: "Metasploit / Backdoor",
    5432: "PostgreSQL",
    5900: "VNC",
    5985: "WinRM (HTTP)",
    5986: "WinRM (HTTPS)",
    6379: "Redis",
    6667: "IRC",
    8000: "HTTP Alt",
    8080: "HTTP Proxy",
    8443: "HTTPS Alt",
    9000: "SonarQube / Dev tools",
    9200: "Elasticsearch",
    11211: "Memcached",
    27017: "MongoDB"
}

fast = asyncio.Semaphore(5000)
async def FastScan(t,p):
    async with fast:
        try:
            r,w=await asyncio.wait_for(asyncio.open_connection(t,p),timeout=4)
            if p in COMMON_PORTS:
                print(f"[*] PORT=> {p} OPEN {COMMON_PORTS[p]}")
            w.close()
            await w.wait_closed()
        except Exception as e:
            pass
async def main():
    t=input("Enter url (example.com): ")
    p = range(20,5000)
    s=[FastScan(t,i) for i in p]
    await asyncio.gather(*s)
    print("Port scannig Fnished")
def PortScan():
    asyncio.run(main())


