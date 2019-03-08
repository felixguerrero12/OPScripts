import sys
import os
import requests
import json


def results(email):
    headers = {'Accept': 'application/vnd.haveibeenpwned.v2+json', 'User-Agent': 'Pwnage-Checker-For-iOS'}
    r = requests.get('https://haveibeenpwned.com/api/v2/pasteaccount/' + str(email), headers=headers)
    if r.status_code == 200:
        data = json.dumps(r.json(), indent=4)
        return data
    else:
        print r.status_code
        return(email + "show no evidence of it being pwned")


def main(argv):
    email = "email.txt"
    if os.path.exists(email) and os.path.getsize(email) > 0:
        with open(email, 'r') as f:
            w_str = f.read().splitlines()
    else:
        w_str = list(sys.argv[1:])
    for i in w_str:
        print(results(i))

if __name__ == "__main__":
    main(sys.argv)
