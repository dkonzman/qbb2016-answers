#!/usr/bin/env python

import sys, fasta 
import scipy
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

"""
Counts synonymous (dS) and non-synonymous (dN) mutations
./dS-dN.py  rev_transl.tsv  week1_query.fa


this code seems to be giving numbers that are very off from what i'd expect.  
I think some sort of frame shift occured in either our alignment or our reverse translation, but otherwise i think this code works for what it should do
"""

nts = open(sys.argv[1])
query = sys.stdin


codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }

for ident, sequence in (fasta.FASTAReader(query)):
    qseq = sequence  #stores whole query nt seq in qseq variable for referencing
#print qseq


mutations = {} 
#key: codon number, value: [dS, dN]
for line in nts:    #reads sequences from aligned nt sequences in file
    fields = line.rstrip("\r\n").split("\t")

    hcount = 0      #count to determine which nt to read as first in a codon in aligned sequences
    qcount = 0      #count to track analagous position in query sequence
    
    if len(fields[1]) > 10000:
        if qcount in mutations:
            mutations[qcount][0] += 1
        mutations[qcount] = [1, 0]
    
        for nt in fields[1]:
            if (hcount+3)%3 != 0:  #this ensures it reads codons in one reading frame, not all 3
                pass
            else: 
                hcodon = fields[1][hcount:hcount+3]   #defines each 3nt codon from aligned nt sequences
                qcodon = qseq[qcount:qcount+3]
                if len(hcodon) < 3:         
                    qcount += 3
                    #print"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
                    pass
                elif len(qcodon) < 3:
                    qcount += 3
                    #print "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
                    pass
                elif hcodon == "---":     #skip gaps, dont add to qcount so positions stay aligned
                    #print "oooooooooooooooooooooooooooooooooooo"
                    pass
                elif hcodon not in codontable:      #skips errors I didn't specifically account for
                    qcount += 3
                    pass
                elif hcodon == qcodon:  #no mutation
                    qcount+=3
                else: 
                    if codontable[hcodon] == codontable[qcodon]:    #if they code for same aa
                        if qcount in mutations:
                            mutations[qcount][0] += 1
                        else:
                            mutations[qcount] = [1, 0]
                    else:                                       #if they code for different aas
                        if qcount in mutations:
                            mutations[qcount][1] += 1
                        else: 
                            mutations[qcount] = [0, 1]
                    qcount+=3
                #print qcount, qcodon, hcount, hcodon

            hcount+=1       #count to track position in sequence and stay in reading frame

#print mutations


a = []
ldiff = []
for key in mutations:
    diff = (mutations[key][1] - mutations[key][0])
    ldiff.append(diff)
    a.append(key)

b = np.array(ldiff)
    
zscores = scipy.stats.mstats.zscore(b)

colors = []
for item in zscores:
    if item >3:
        colors.append("red")
    elif item <-3:
        colors.append("red")
    else:
        colors.append("blue")

        
plt.figure()
plt.scatter(a, zscores, c=colors, edgecolor="none")
plt.title("dN-dS distribution")
plt.xlabel("Position in query sequence")
plt.ylabel("Z-score")
#plt.show()
plt.savefig("zscore_scatterplot.png")
plt.close()
    
    
    
    
        