import sys
import os
import requests
import json

def results(ipaddr):
	params = {'ip': ipaddr, 'apikey': 'API_KEY HERE'}
	headers = {
  		"Accept-Encoding": "gzip, deflate",
  	"User-Agent" : "gzip,  My python example client or username"
	}
	response = requests.get('https://www.virustotal.com/vtapi/v2/ip-address/report',
  	params=params, headers=headers)
	response_json = json.dumps(response.json(), indent=2, sort_keys=True)
	return response_json

def main(argv):
    ipaddr = "ipaddr.txt"
    if os.path.exists(ipaddr) and os.path.getsize(ipaddr) > 0:
        with open(ipaddr, 'r') as f:
            w_str = f.read().splitlines()
    else:
        w_str = list(sys.argv[1:])
    with open("output.txt", 'w') as f:
        for i in w_str:
            f.write('IPAddr: '+i + '\n')
            f.write(results(i) + '\n')


if __name__ == "__main__":
    main(sys.argv)
