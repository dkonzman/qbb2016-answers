#!/usr/bin/env python

import sys

count = 0
totmapq = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    else:
        col = line.split("\t")[4]
        if col == "255" or len(line.split("\t")) < 5:
            continue
        else:
            totmapq = totmapq + int(col)
            count += 1
            
average = float(totmapq) / float(count)

print average

            
