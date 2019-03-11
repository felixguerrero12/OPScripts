#! /usr/bin/python
from scapy.all import *
import sys


def capture(pkt):
        if IP in pkt:
                ip_src = pkt[IP].src
                ip_dst = pkt[IP].dst
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                    print(ip_src + " - > " + ip_dst + " " + "Domain requested: " + str(pkt.getlayer(DNS).qd.qname))
                elif pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
                    ret = "\n".join(pkt.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
                    print(ret)

def main():
	interface = 'en0'
	sniff(iface = interface, prn = capture, store = 0)
	print("\n[*] Shutting Down...")

if __name__ == "__main__":
    main()
