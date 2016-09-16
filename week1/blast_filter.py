#!/usr/bin/env python

"""removes -s from blast output"""


import sys

for line in sys.stdin:
    fields = line.rstrip("\r\n").split("\t")
    fields[2] = fields[2].replace("-", "")
    if fields[1] == '1' and fields[2] == '10293':
        print ">", fields[0]
        print fields[3]
        