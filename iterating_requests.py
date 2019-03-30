import requests

for i in range(2,999):
	r = requests.get('http://example.org/forensics/Castles.' + f'{i:03}')
	if r.status_code == 200:
		print(r.text)
