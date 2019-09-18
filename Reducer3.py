#!/usr/bin/env python
import sys

citation_count = 0
patent_info = None
last_patent_id = None

# citing id    1
# or
# patent id    info
for line in sys.stdin:

	line = line.strip()

	line = line.split('\t')

	patent_id = line[0]

	if last_patent_id != patent_id:

		if citation_count != 0 and patent_info is not None:
			print "{},{},{}".format(patent_info[0], patent_info[1], citation_count)

		last_patent_id = patent_id

		citation_count = 0
		patent_info = None

	# it's citing id    1
	if line[1] == "1":
		citation_count += 1
	else:
		patent_info = (line[0], line[1])

if citation_count != 0 and patent_info is not None:
	print "{},{},{}".format(patent_info[0], patent_info[1], citation_count)