#!/usr/bin/env python

import sys

count = 0
b = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    else:
        while b<10:
            linelist = line.split("\t")
            print linelist[2]
            b+=1
            
