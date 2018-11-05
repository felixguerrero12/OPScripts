import json
import passgen
import sys


def gen(passwords):
    for i in range(5):
	    passwords[i] = passgen.gen(15)
    results = {"passwords": passwords}
    return results


def main(argv):
    passwords = {}
    print (gen(passwords))


if __name__ == "__main__":
    main(sys.argv)