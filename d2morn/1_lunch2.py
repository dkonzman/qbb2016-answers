#!/usr/bin/env python

import sys


count = 0
for line in sys.stdin:
    if line.startswith("@"):
        continue
    else:
        count += 1
print count