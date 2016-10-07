#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

"""./histo.py < allelefreq.frqx"""

file = sys.stdin

allelefreq = []

for line in file:
    if line.startswith("CHR"):
        continue
    fields = line.rstrip("\r\n").split("\t")
    minor = float(fields[4])
    major = float(fields[6])
    allelefreq.append( (minor / (minor + major)))
    

plt.figure()
plt.hist(allelefreq)
#plt.show()
plt.title("Minor allele frequencies")
plt.savefig("allele_freq_histo.png")
plt.close()    