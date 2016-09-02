#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import statsmodels.api as sm

#useage:  ./regression.py  histone.tab  t_data.ctab

df = pd.read_table(sys.argv[1])

df2 = pd.read_table(sys.argv[2]) 

#dictionary of t_names in histone tab file, [mean_signal, fpkm]
d = {}

for i in df.itertuples():
    name = i[1]
    signal = i[6]
    d[name] = [signal]
    
for i in df2.itertuples():
    name = i[6]
    fpkm = i[-1]
    if name in d:
        d[name].append(fpkm)

#print d
signal_list = []
fpkm_list = []

for key in d.keys():
    signal = d[key][0]
    fpkm = d[key][1]
    signal_list.append(signal)
    fpkm_list.append(fpkm)


model = sm.OLS(signal_list, fpkm_list)
res = model.fit()
print res.summary()



#X = sm.add_constant()
#Y = signal_list
