#!/usr/bin/env python

"""
take the multiple-sequence alignment and rev-translate into nucleotide sequence, including gaps
use the MSA and refer back to alignment.tsv??
MSA file has >ID (eg >WNFCG_1), \n, aa seq with spaces
alignment.tsv looks like:   gi|148925303|gb|EF429200.1|     1       10293   ATGTCTAAG
"""


import sys, fasta, itertools

#  aa_to_nt.py  < msa.fa  fasta_nodashes.fa 

align = open(sys.argv[1])
fast = sys.stdin

laa = []
lnt = []


for ident, sequence in (fasta.FASTAReader(fast)):
    laa.append((ident, sequence))
    
for line in align:
    fields = line.rstrip("\r\n").split(" ")
    lnt.append((fields[0],fields[2]))    


    
for thing in itertools.izip(lnt, laa):
    nuc_s = thing[0][1]
    pro_s = thing[1][1]
    s = ""
    n = 0
    for aa in pro_s:
        if aa == "-":
            s += "---"
        else: 
            codon = nuc_s[n:n+3]
            n += 3
            s += codon
    print thing[1][0], "\t", s
            
