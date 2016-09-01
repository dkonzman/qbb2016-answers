#!/usr/bin/env python 

import sys, fasta

#in format: ./.py txtfile 
#in format: ./match-extender.py  all-11mer-matches  droYak
#out format: target_loc, extended_kmer_sequence, ident

data = open(sys.argv[1])
query = sys.argv[2]

sequential_hits = {}


count = 0
for line in data:
    fields = line.rstrip("\r\n").split()
    k = len(fields[3])
    broken = False
    for key in sequential_hits:
        if fields[0] in key:
            if int(fields[2]) == int(sequential_hits[key][-1])+1:
                sequential_hits[key].append(fields[2])
                broken = True
                break
    if broken:
        pass
    else:
        count += 1
        sequential_hits[fields[0] + str(count)] = [int(fields[2])]

print fields[3]                


kmers = []  
for (identifier, hits) in sequential_hits.iteritems():
    #print len(sequential_hits[hits])
    for ident, sequence in (fasta.FASTAReader(open(query))):
        kmer = sequence[hits[0] : hits[0] + len(hits) + k - 1]
        kmers.append((len(kmer), identifier, hits[0], kmer))
kmers.sort(reverse=True)
for h in kmers:
    print "ID: ", h[1], "location: ", h[2], "sequence: ", h[3]
    
        
        
#print sequential_hits[hits][0], 