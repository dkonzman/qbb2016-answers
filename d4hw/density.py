#!/usr/bin/env python

#Useage: ./script.py  893.ctab

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

df = pd.read_table(sys.argv[1])
f = df["FPKM"].values

density = gaussian_kde(f)

xs = np.linspace(min(f), 200, 100)
plt.plot(xs,density(xs))
#plt.show()
plt.savefig("densityplot.png")
plt.close()
