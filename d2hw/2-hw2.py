#!/usr/bin/env python

import sys

#dictionary construction, taking first file as argument

gene_names_dict = {}

f = open(sys.argv[1])
for line in f:
    a = line.rstrip("\r\n").split("\t")
    gene_names_dict[a[1]] = a[0]


#comparing .ctab file (as second arg from bash) to dict created above

g = open(sys.argv[2])
for lines in g:
    a = lines.rstrip("\r\n").split("\t")
    if a[8] in gene_names_dict:
        print '\t'.join(a), gene_names_dict[a[8]]  #when two files are the only args, prints only those that match
    else: 
        if len(sys.argv) > 3:  #adding extra arguments is an option to print all those that do not match with an X
            print '\t'.join(a), "X"

        