#!/usr/bin/python
# -*- coding: utf-8 -*-


def count_dict(mystring):
    d = {}
    for w in mystring:
        d[w] = mystring.count(w)
    for k in sorted(d):
        print (k + ': ' + str(d[k]))


def main():
    f=open("occurences.txt", "r")
    if f.mode == 'r':
	    contents=f.read()
    print(count_dict(contents))


if __name__ == "__main__":
    main()
