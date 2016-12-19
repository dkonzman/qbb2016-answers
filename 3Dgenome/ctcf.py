#!/usr/bin/env python

import h5py, sys
import numpy as np

peaks = sys.stdin

file = h5py.File("Out.heat")
counts = file['0.counts'][...]
expected = file['0.expected'][...]
positions = file['0.positions'][...]
regions = file['regions'][...]


counts1 = np.ma.masked_equal(counts,0)
expected1 = np.ma.masked_equal(expected,0)

enrichments = np.log(counts1/expected1)
enrichments = np.ma.filled(enrichments,0)

#print enrichments
#print positions
#print regions

peaks_dict = {}
for i, line in enumerate(peaks):
    fields = line.rstrip("\r\n").split("\t")
    chrom = fields[0]
    pos = fields[1]
    if chrom == 'chrX':
        peaks_dict[pos] = int(pos)

#print peaks_dict

for i, line in enumerate(positions):
    for p in peaks_dict: 
        if int(p) >= line[0] and int(p) <= line[1]:
            k=0
            for anum, line2 in enumerate(enrichments):
                k+=1
                if k == 1:
                    maximum = anum
                    position = line2
                elif anum > maximum:
                    maximum = anum
                    position = line2
            print i, position
    
# and pos >= 98831147 and pos <= 103425148