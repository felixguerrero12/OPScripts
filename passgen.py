import random
import string
import sys


def gen(pw_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(characters))
        mypw += characters[next_index]
    return mypw


def main(argv):
    pw_length = int(argv[1]) if len(argv) > 1 else 15
    print(gen(pw_length))


if __name__ == "__main__":
    main(sys.argv)
