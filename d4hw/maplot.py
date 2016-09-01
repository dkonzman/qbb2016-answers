#!/usr/bin/env python

#Useage: ./script.py  893.ctab  915.ctab  

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])


f1 = df1["FPKM"].values+1
f2 = df2["FPKM"].values+1

m = np.log2(f1/f2)
a = 0.5*np.log2(f1*f2)







plt.figure()
plt.scatter( a, m )
plt.title("MA plot of FPKM values between SRR072893 & SRR072915")
plt.xlabel("A")
plt.ylabel("M")
#plt.show()
plt.savefig("MA_plot.png")
plt.close()
