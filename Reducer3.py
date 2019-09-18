#!/usr/bin/env python
import sys

citation_count = 0
patent_info = None

# citing id    1
# or
# patent id    info
for line in sys.stdin:

	line = line.strip()

	line = line.split('\t')

	# it's citing id    1
	if line[1] == "1":
		citation_count += 1
	else:
		patent_info = (line[0], line[1])

if citation_count != 0 and patent_info is not None:
	print "{},{},{}".format(patent_info[0], patent_info[1], citation_count)