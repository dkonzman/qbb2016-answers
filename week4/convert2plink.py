#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

""""""


for line in sys.stdin:
    if line.startswith("\t"):
        print "FID", "\t", "IID", line.rstrip("\r\n")
        continue
    fields = line.rstrip("\r\n").split("\t")
    print fields[0][0:3], "\t", fields[0][4:], "\t", "\t".join(fields[1:])
