#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

#print df

df_roi = df["gene_name"] == "Sxl"
df_sxl = df[df_roi]
df_values = df["FPKM"] > 0 
df_sxlfpkm = df_sxl[df_values]
#print df_sxlfpkm

df2_roi = df2["gene_name"] == "Sxl"
df2_sxl = df2[df2_roi]
df2_values = df2["FPKM"] > 0 
df2_sxlfpkm = df2_sxl[df2_values]
#print df2_sxlfpkm

#df_sxlfpkm["FPKM"]
#df_sxlfpkm["FPKM"]

#d1 = df_sxlfpkm["FPKM"]
#d2 = df2_sxlfpkm["FPKM"]
d1 = np.log10(df_sxlfpkm["FPKM"])
d2 = np.log10(df2_sxlfpkm["FPKM"])

dev_stage = ["SRR072893", "SRR072915"]

plt.figure()
plt.title("Sxl transcript abundance")
plt.boxplot(
[d1, d2],
labels=dev_stage,    
)
plt.xlabel("developmental stage")
plt.ylabel( "log10 FPKM" )
plt.savefig("sxl_abundance.png")
plt.close()