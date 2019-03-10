#! /usr/bin/python

from scapy.all import *
import sys

try:
        interface = 'en0'
except KeyboardInterrupt:
        print("[*] User Requested Shutdown...")
        print("[*] Exiting...")
        sys.exit(1)

def capture(pkt):
        if IP in pkt:
                ip_src = pkt[IP].src
                ip_dst = pkt[IP].dst
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                        print(ip_src + " - > " + ip_dst + " " + "Domain requested: " + str(pkt.getlayer(DNS).qd.qname))

sniff(iface = interface, prn = capture, store = 0)
print("\n[*] Shutting Down...")
