import requests

headers = {
    'accept': 'application/json',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
}

data = {
  'grant_type': 'client_credentials',
  'client_id': 'CLIENT_ID'
  'client_secret': 'CLIENT_SECRET'
  'scope': 'customScope'
}

response = requests.post('https://authorization-server.com/oauth2/default/v1/token', headers=headers, data=data)
print response.text
