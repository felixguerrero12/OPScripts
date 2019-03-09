#!/usr/bin/python
# -*- coding: utf-8 -*-

def count_dict(filename):
    f = open(filename,'r')
    words_dict={}
    for i in f.read().split():
        word=i.lower()
        words_dict[word]= words_dict.get(word,0) + 1
    for key in words_dict.keys():
        print str(key)+' = '+str(words_dict[key])

def main():
    filename="occurences.txt"
    count_dict(filename)

if __name__ == "__main__":
    main()
