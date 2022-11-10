import sys
import os
import requests
import json


def results(ipaddr):
    r = requests.get(
        f'http://ip-api.com/json/{str(ipaddr)}?fields=status,country,countryCode,reverse,query'
    )

    return json.dumps(r.json(), indent=4)


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
