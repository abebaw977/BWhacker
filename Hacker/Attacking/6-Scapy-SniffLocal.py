from scapy.all import sniff, IP, TCP, UDP, ICMP, wrpcap
from datetime import datetime

pack = []

def packet(pkt):
    time = datetime.now().strftime("%H:%M:%S")
    size = len(pkt)

    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = pkt[IP].proto

        if proto == 6 and TCP in pkt:  # TCP
            protocol = "TCP"
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport
        elif proto == 17 and UDP in pkt:  # UDP
            protocol = "UDP"
            sport = pkt[UDP].sport
            dport = pkt[UDP].dport
        elif proto == 1 and ICMP in pkt:  # ICMP
            protocol = "ICMP"
            sport = "-"
            dport = "-"
        else:
            protocol = str(proto)
            sport = "-"
            dport = "-"

        print(f"[{time}] {src}:{sport} -> {dst}:{dport} | {protocol} | {size} bytes")

    pack.append(pkt)

def main():
    iface = input("Enter network interface (eg eth0, wlan0): ").strip()
    filter_proto = input("Enter one of these (eg tcp, udp, icmp): ").strip()

    print(f"\nSniffing on {iface} ... Press CTRL+C to stop.\n")
    try:
        sniff(iface=iface, prn=packet_callback, filter=filter_proto, store=False)
    except PermissionError:
        print("run as root")
    except KeyboardInterrupt:
        print("\nStopping capture...")
        save = input("Save packets to file (y/n)? ").lower()
        if save == "y":
            f = f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pcap"
            wrpcap(f, packets)
            print(f"Packets saved to {f}")

if __name__ == "__main__":
    main()
