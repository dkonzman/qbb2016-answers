#!/usr/bin/env python

import sys

count = 0
for line in sys.stdin:
    if "ZS:i:" in line:
        continue
    elif "AS:i" in line:
        count += 1
print count
    
    