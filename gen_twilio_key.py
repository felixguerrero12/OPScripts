from twilio.rest import Client


account_sid = ''
auth_token = ''


def gen_key(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    new_key = client.new_keys.create()
    print(f'Account SID: {account_sid}')
    print(f'Authentication token: {auth_token}')
    print(f'API Key: {new_key.sid}')


def main(account_sid, auth_token):
    gen_key(account_sid, auth_token)


if __name__ == "__main__":
    main(account_sid, auth_token)
