from Cryptodome.PublicKey import RSA
import sys


def key_generate(key_size):
    key = RSA.generate(key_size)
    with open("private.pem", "wb") as pubhandle:
        pubhandle.write(key.export_key())

    with (open("receiver.pem", "wb")) as privhandle:
        privhandle.write(key.publickey().export_key())

def main(argv):
    key_size = 2048
    key_generate(key_size)

if __name__ == "__main__":
    main(sys.argv)