#! /usr/bin/python
from scapy.all import *
import sys


try:
        interface = 'en0'
except KeyboardInterrupt:
        print("[*] User Requested Shutdown...")
        print("[*] Exiting...")
        sys.exit(1)


def dns(pkt):
        if IP in pkt:
                src = pkt[IP].src
                dst = pkt[IP].dst
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                        print(src + " - > " + dst + " " + "request: " + str(pkt.getlayer(DNS).qd.qname))


sniff(iface = interface,filter = "port 53", prn = dns, store = 0)
