#!/usr/bin/python
# -*- coding: utf-8 -*-


def count_dict(mystring):
    d = {w: mystring.count(w) for w in mystring}
    for k in sorted(d):
        print(f'{k}: {str(d[k])}')


def main():
    f=open("occurences.txt", "r")
    if f.mode == 'r':
	    contents=f.read()
    count_dict(contents)


if __name__ == "__main__":
    main()
