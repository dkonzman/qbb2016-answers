#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

""" manhattan.py  *.qassoc """

for f in sys.argv[1:]:
    
    title = f.split(".")[1]

    x = []
    y = []

    x2 = []
    y2 = []

    for i, line in enumerate(open(f)):
        if i == 0:
            continue
        fields = line.rstrip("\r\n").split()
        if float(fields[-1]) < 0.00001:
            x2.append(i)
            y2.append(- np.log10(float(fields[-1])) )
        x.append(i)
        y.append(- np.log10(float(fields[-1])) )

    plt.figure()
    plt.plot(x,y,"b.")
    plt.plot(x2,y2,"r.")
    plt.title("Manhattan plot %s" % title)
    #plt.show()
    plt.savefig("Manhattan_%s.png" % title)
    plt.close()

