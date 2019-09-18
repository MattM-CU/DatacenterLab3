#!/usr/bin/env python
import sys

# this is basically cat
for line in sys.stdin:

	line = line.strip()

	if line:

		print line
