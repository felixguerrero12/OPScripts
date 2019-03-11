#! /usr/bin/python
from scapy.all import *
import sys

def extract_headers_from_request_payload(payload):
    try:
        return payload.split('\r\n\r\n')[0].split('\r\n')
    except ValueError:
        return payload.split('\r\n')

def find_url_from_headers(headers):
    host = ''
    uri = ''
    method = headers[0][0:headers[0].find('/')].strip()
    for line in headers:
        # find host & uri
        if 'Host: ' in line:
            host = line.split('Host: ')[1].strip()
        if ('%s /' % method) in line:
            uri = line.split('%s ' % method)[1].split(' HTTP/')[0].strip()
    return ''.join([host, uri])


def capture(pkt):
        if IP in pkt:
                ip_src = pkt[IP].src
                ip_dst = pkt[IP].dst
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                    print(ip_src + " - > " + ip_dst + " " + "Domain requested: " + str(pkt.getlayer(DNS).qd.qname))
                elif pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
                    payload = pkt[Raw].load.decode('utf-8', 'ignore')
                    print(ip_src + " - > " + ip_dst + " " + "Full URL: " + find_url_from_headers(extract_headers_from_request_payload(payload)))

#                    ret = "\n".join(pkt.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
#                    print(ret)
def main():
	interface = 'en0'
	sniff(iface = interface, prn = capture, store = 0)
	print("\n[*] Shutting Down...")

if __name__ == "__main__":
    main()
