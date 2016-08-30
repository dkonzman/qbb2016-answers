#!/usr/bin/env python

import sys

for line in sys.stdin:
    if "DROME" in line:
        strline = line.rstrip("\n")
        first_space = strline[(len(strline)-23):(len(strline)-13)]
        uniprot = strline[(len(strline) - 11):]
        flybase = first_space.strip(" ")
        print flybase, "\t", uniprot
        
        
        #flybase = bothcol[0:10]
        #uniprot = bothcol[12:]
        #print flybase, "\t", uniprot
        
        
        #print "".join(flybase), "\t", uniprot
        
        #for char in strline:
        #    if char = " "
        