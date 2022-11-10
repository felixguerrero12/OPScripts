import ipaddress
import sys
import os


def print_rule(x):
    print(
        f"netsh advfirewall firewall add rule name={str(x)} dir=in interface=any action=block remoteip={str(x)}"
    )


def main(argv):
    whitelist = "wipaddr.txt"
    if os.path.exists(whitelist) and os.path.getsize(whitelist) > 0:
        with open(whitelist, 'r') as f:
            w_str = f.read().splitlines()
    else:
        w_str = list(sys.argv[1:])
    x = list(ipaddress.IPv4Network(u'192.168.1.0/24'))[1:-1]
    for ip in x:
        if str(ip) not in w_str:
            print_rule(ip)


if __name__ == "__main__":
    main(sys.argv)
