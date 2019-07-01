import requests
import sys
import json

def results(domain):
        api_key = "INPUT API HERE"
        headers = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        }
        response = requests.get('https://api.hunter.io/v2/domain-search?domain=' + domain +
                '&api_key='+ api_key + '&limit=100')
        data = response.json()
        return data


def main(argv):
    domain = sys.argv[1]
    output = results(domain)
    for i in output['data']['emails']:
        print("{0} {1},{2}".format(i['first_name'], i['last_name'],i['value']))


if __name__ == "__main__":
    main(sys.argv)
