#! /usr/bin/env python

'''find what genes are differentially expressed between the first two stages and the last two stages'''

import sys
from scipy import stats



diffexpr = []

for line in sys.stdin:  #finds genes with 2fold diff between cfu and unk
    fields = line.strip().split('\t')
    if fields[1] == "CFU":
        continue
    if fields[2] > 2*float(fields[1]) or fields[2] < 0.5*float(fields[1]):
        diffexpr.append(fields[0])
    else:
        continue
        
print diffexpr
        