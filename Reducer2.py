#!/usr/bin/env python
import sys

citations = list()
cited_state = None
last_patent_id = None

# cited id    C-citing id,citing state
# or
# patent id    S-state
# or
# patent id    info
for line in sys.stdin:

	line = line.strip()

	line = line.split('\t')

	patent_id = line[0]

	if patent_id != last_patent_id:
		if cited_state is not None:
			for citation in citations:
				# citing id    citing state    cited id    cited state
				print "{}\t{}\t{}\t{}".format(citation[0], citation[1], citation[2], cited_state)

		last_patent_id = patent_id

		cited_state = None
		citations = list()

	# it's patent id   S-State
	if line[1].startswith('S'):

		cited_state = line[1].split('-')[1]

	# it's cited id    C-citing id,citing state
	elif line[1].startswith('C'):

		cited_id = line[0]

		citing_id_state = line[1].split('-')[1].split(',')

		citing_id = citing_id_state[0]
		citing_state = citing_id_state[1]

		citations.append((citing_id, citing_state, cited_id))

	# it's patent id    info
	else:
		# patent id    info
		print "{}\t{}".format(line[0], line[1])

if cited_state is not None:
	for citation in citations:
		# citing id    citing state    cited id    cited state
		print "{}\t{}\t{}\t{}".format(citation[0], citation[1], citation[2], cited_state)