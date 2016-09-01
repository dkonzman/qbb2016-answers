#!/usr/bin/env python

#Useage: ./script.py .ctab

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table(sys.argv[1])



fpkm_values = df["FPKM"] > 0 
fpkm_nonzero = df[fpkm_values]["FPKM"]

t_values = df[fpkm_values]["t_name"] 
log_values = np.log10(fpkm_nonzero)

plt.figure()
plt.hist( log_values, bins=30)
#plt.plot( male_Sxl, color="b" )
#plt.scatter( replica, fem_reps_Sxl, color="r")
#plt.scatter( replica, male_reps_Sxl, color="b")
plt.title("FPKM values for SRR072893")
plt.xlabel("transcript name")
plt.ylabel("log FPKM")
#plt.show()
plt.savefig("histo.png")
plt.close()
