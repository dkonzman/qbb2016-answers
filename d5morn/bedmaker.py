#!/usr/bin/env python

# Usage: ./bedmaker.py  t_data.ctab


import sys
import pandas as pd
import numpy as np

df = pd.read_table(sys.argv[1])


lst = []

for i in df.itertuples():
    strand = i[3]
    chr = i[2]
    if chr in ["2L", "2R", "3L", "3R", "4", "X", "Y"]:
        t_name = i[6]
        if strand == "+":
            start = int(i[4]) - 500
            end = int(i[4]) + 500
            lst.append((chr, start, end, t_name))
        elif strand == "-":
            start = int(i[5]) + 500
            end = int(i[5]) - 500
            lst.append((chr, start, end, t_name))
            
    
df = pd.DataFrame(lst)
df.columns = ["chrom", "Start", "End", "t_name"]
df.to_csv("promoter_reg.bed", sep="\t", header=None, index=None)


 