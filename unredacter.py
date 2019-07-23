import sys

def unredacter(unredacted_ip, ip):
    for i in range(len(unredacted_ip)):
        if unredacted_ip[i].isdigit() == True :
            ip.append(unredacted_ip[i])
        elif unredacted_ip[i] == ".":
            ip.append(unredacted_ip[i])
        else:
            pass
    cleaned_ip = "".join(ip)
    verify_format(cleaned_ip)

def verify_format(cleaned_ip):
    if cleaned_ip.count('.') == 3:
        ip_pieces = [ip_section for ip_section in cleaned_ip.split('.')]
        if len(ip_pieces) == 4:
            for ip_section in ip_pieces:
                if not 0<= int(ip_section) <= 255:
                    print "Invalid ip address: " + cleaned_ip +" due to " + ip_section
        else:
            print "Invalid format #2 - Not enough numbers"

    else:
        print "Invalid Format #1 - Not enough dots"


def main(argv):
    ip = []
    unredacted_ip = argv[1]
    unredacter(unredacted_ip, ip)


if __name__ == "__main__":
    main(sys.argv)
