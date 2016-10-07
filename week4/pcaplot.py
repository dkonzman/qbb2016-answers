#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

"""./pcaplot.py < eigenvec"""


eigenvec = sys.stdin

x = []
y = []
for line in eigenvec:
    fields = line.rstrip("\r\n").split(" ")
    x.append(fields[2])
    y.append(fields[3])


plt.figure()
plt.scatter(x,y)
plt.title("PCA of genotype data")
plt.savefig("genoPCA.png")
plt.close()