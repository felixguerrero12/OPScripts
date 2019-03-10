#! /usr/bin/python
from scapy.all import *
import sys


def capture(pkt):
        if IP in pkt:
                ip_src = pkt[IP].src
                ip_dst = pkt[IP].dst
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                        print(ip_src + " - > " + ip_dst + " " + "Domain: " + str(pkt.getlayer(DNS).qd.qname))

def main():
	interface = 'en0'
	sniff(iface = interface, prn = capture, store = 0)
	print("\n[*] Shutting Down...")

if __name__ == "__main__":
    main()
