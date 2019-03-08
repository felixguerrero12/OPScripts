import sys
import os
import requests
import json
from pandas.io.json import json_normalize


def results(ipaddr):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
	r = requests.get('http://api.ipstack.com/' + str(ipaddr)
	+ '?access_key=[key]'
	+ '&hostname=1'
	+ ', headers=headers')
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
