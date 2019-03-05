import sys, ipaddress


def print_rule_input(x):
    print "iptables -A INPUT -p tcp -s " + str(x) + " -j ACCEPT"


def print_rule_output(x):
    print "iptables -A OUTPUT -p tcp -s " + str(x) + " -j ACCEPT"


def print_closure():
    return "iptables -A INPUT -j DROP" + "\n" + "iptables -A OUTPUT -j DROP"


def main(argv):
    w_str = list(sys.argv[1:])
    x = list(ipaddress.IPv4Network('192.168.1.0/24'))[1:-1]
    for ip in x:
	if str(ip) in w_str:
	    input_table = print_rule_input(ip)
	    output_table = print_rule_output(ip)
    print print_closure()


if __name__ == "__main__":
    main(sys.argv)
