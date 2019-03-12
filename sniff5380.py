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
               if pkt.haslayer(DNS):
                   if pkt.getlayer(DNS).qr == 0:
                       print(pkt['IP'].src + " - > " + pkt['IP'].dst + " " + "Domain requested: " + str(pkt.getlayer(DNS).qd.qname))
                   elif pkt.getlayer(DNS).qr == 1:
                       try:
                           domain_request = str(pkt[DNS].qd.qname)
                       except:
                           domain_request = " "
                       try:
                           domain_rdata = str(pkt[DNS].an.rdata)
                       except:
                           domain_rdata = " "
                       print(domain_request + " " +  "translates to:" + " " +  " " + domain_rdata)
               elif pkt.haslayer(TCP) and pkt.getlayer(TCP).dport == 80 and pkt.haslayer(Raw):
                    payload = pkt[Raw].load.decode('utf-8', 'ignore')
                    print(ip_src + ":" + str(pkt[TCP].sport) +" - > " + ip_dst + ":" +
			    str(pkt[TCP].dport) + " " + "Full URL: " + find_url_from_headers(extract_headers_from_request_payload(payload)))
               else:
                    if pkt[IP].proto == 6:
                        print("TCP Communications: " + pkt[IP].src + ":" + str(pkt[TCP].sport)
				+" -> " + pkt[IP].dst + ":" + str(pkt.getlayer(TCP).dport))
                    elif pkt[IP].proto == 17:
                        print("UDP Communications: " + pkt[IP].src + ":" + str(pkt[UDP].sport)
				+" -> " + pkt[IP].dst + ":" + str(pkt.getlayer(UDP).dport))

def main():
	interface = 'en0'
	sniff(iface = interface, prn = capture, store = 0)
	print("\n[*] Shutting Down...")

if __name__ == "__main__":
    main()
