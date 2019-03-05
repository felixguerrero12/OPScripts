import sys, ipaddress


def print_rule(x):
    print "netsh advfirewall firewall add rule name=" + str(x) + " dir=in interface=any action=block remoteip=" + str(x)


def main(argv):
    w_str = list(sys.argv[1:])
    x = list(ipaddress.IPv4Network('192.168.1.0/24'))
    for ip in x:
	if str(ip) not in w_str:
	    print_rule(ip)


if __name__ == "__main__":
    main(sys.argv)
