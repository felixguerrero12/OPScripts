import sys
import os
import requests
import json

def results(ipaddr):
    r = requests.get('http://api.ipstack.com/' + str(ipaddr) + '?access_key=[KEY]&fields=success,country_name,continent_code,ip,&output=json')
    data = json.dumps(r.json(), indent=4)
    return data


def main(argv):
    ipaddr = "ipaddr.txt"
    if os.path.exists(ipaddr) and os.path.getsize(ipaddr) > 0:
        with open(ipaddr, 'r') as f:
            w_str = f.read().splitlines()
    else:
        w_str = list(sys.argv[1:])

    for i in w_str:
	print(results(i))

if __name__ == "__main__":
    main(sys.argv)
