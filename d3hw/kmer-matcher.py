#!/usr/bin/env python 

import sys
import fasta


#in format: kmer_matcher.py <target.fa> <query.fa> <k>
#in format: kmer_matcher.py subset.fa droYak2_seq.fa <k>

#out format: target_sequence_name    target_start    query_start k-mer


target_fa = open(sys.argv[1])
query_fa = open(sys.argv[2])
k = int(sys.argv[3])

kmer_loci = {}

#generates dictionary of kmers from target file, { key = kmer, value = list of loci }
for ident, sequence in (fasta.FASTAReader(target_fa)):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in kmer_loci:
            kmer_loci[kmer] = [ident, i]
        else:
            kmer_loci[kmer].append(i)

#generate sequential kmers from query, check if in kmer_loci dict, then print results
for ident2, sequence2 in (fasta.FASTAReader(query_fa)):
    sequence2 = sequence2.upper()
    for i in range(0, len(sequence2) - k):
        kmer = sequence2[i:i+k]
        if kmer in kmer_loci:
            print kmer_loci[kmer][0], kmer_loci[kmer][1:], i, kmer
        

        
#for kmer, loci in kmer_loci.iteritems():
#    print ident, kmer, loci
    
    
    
    
    

""" print "----", ident, "----"
    for i, kmer in enumerate(sorted(kmer_counts, key=kmer_counts.get, reverse=True)):
        if i >10:
            break
        print kmer, kmer_counts[kmer]"""
	