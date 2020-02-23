#!/usr/bin/env python
# Modified from original location: https://gist.github.com/superkojiman/11076951
import sys

if __name__ == "__main__":
        if len(sys.argv) != 3:
                print "usage: %s names.txt domain.com" % (sys.argv[0])
                sys.exit(0)

        domain = sys.argv[2]

        for line in open(sys.argv[1]):
                name = ''.join([c for c in line if  c == " " or  c.isalpha()])

                tokens = name.lower().split()
                fname = tokens[0]
                lname = tokens[-1]

                print fname + lname + "@" + domain              # johndoe
                print lname + fname + "@" + domain             # doejohn
                print fname + "." + lname  + "@" + domain      # john.doe
                print lname + "." + fname  + "@" + domain      # doe.john
                print lname + fname[0] + "@" + domain         # doej
                print fname[0] + lname + "@" + domain          # jdoe
                print lname[0] + fname  + "@" + domain         # djoe
                print fname[0] + "." + lname + "@" + domain   # j.doe
                print lname[0] + "." + fname + "@" + domain   # d.john
                print fname + "@" + domain               # john
                print lname + "@" + domain                   # joe
