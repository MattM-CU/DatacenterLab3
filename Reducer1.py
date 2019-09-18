#!/usr/bin/env python
import sys

citations = list()
citing_state = None
last_patent_id = None

# citing id    C-cited id
# or
# patent id    S-state
# or
# patent id    info
for line in sys.stdin:

	line = line.strip()

	line = line.split('\t')

	patent_id = line[0]

	if patent_id != last_patent_id:
		if citing_state is not None:
			for citation in citations:
				# cited id    C-citing id,citing state
				print "{}\tC-{},{}".format(citation[0], citation[1], citing_state)

		last_patent_id = patent_id

		citing_state = None
		citations = list()

	# it's patent id   S-State
	if line[1].startswith('S'):

		citing_state = line[1].split('-')[1]

		# patent id    S-state
		print "{}\t{}".format(line[0], line[1])

	# it's citing id    C-cited id
	elif line[1].startswith('C'):

		citing_id = line[0]
		cited_id = line[1].split('-')[1]

		citations.append((cited_id, citing_id))

	# it's patent id    info
	else:
		# patent id    info
		print "{}\t{}".format(line[0], line[1])

if citing_state is not None:
	for citation in citations:
		# cited id    C-citing id,citing state
		print "{}\tC-{},{}".format(citation[0], citation[1], citing_state)
