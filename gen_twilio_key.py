from twilio.rest import Client


account_sid = 'AC27c7e6eb55958253856a791b7f00c386'
auth_token = '94002dc1687dd086162621cd5410d64a'


def gen_key(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    new_key = client.new_keys.create()
    print('Account SID: ' + account_sid)
    print('Authentication token: ' + auth_token)
    print('API Key: ' + new_key.sid)


def main(account_sid, auth_token):
    gen_key(account_sid, auth_token)


if __name__ == "__main__":
    main(account_sid, auth_token)
