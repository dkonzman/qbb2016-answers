#!/usr/bin/env python

import sys, fasta


#Using the contigs.fasta file, I want to compute: #contigs, min, max, avg, N50
#N50 is the length of the read that is half of the total of the lengths of all reads
#format:  ./contigstats.py  <  contigs.fa

seqs = []
lengths = []

for ident, sequence in fasta.FASTAReader(sys.stdin):
    seqs.append(sequence)
    lengths.append(len(sequence))

a = 0
for i in lengths:
    a += i    
avg_len = float(a)/float(len(lengths))

b=0
for i in lengths: 
    b += i
    if b > a/2:
        n50 = i
        break


    
print "Number of contigs: ", len(seqs)
print "min: ", len(seqs[-1])
print "max: ", len(seqs[0])
print "avg: ", avg_len
print "N50: ", n50
    