#!/usr/bin/env python

import sys

for line in sys.stdin:
    if "DROME" in line:
        strline = line.rstrip("\n")
        a = strline[(len(strline)-23):]
        print a[0:10], "\t", a[12:]
        
        
        #for char in strline:
        #    if char = " "
        