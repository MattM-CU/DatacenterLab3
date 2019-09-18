#!/usr/bin/env python
import sys

# citing id    citing state    cited id    cited state
# or
# patent id    info

for line in sys.stdin:

	line = line.strip()

	line = line.split('\t')

	# it's citing id    citing state    cited id    cited state
	if len(line) == 4:
		# check if states are the same -- output a 1 so that reduce can count them
		if line[1] == line[3]:
			# citing id    1
			print "{}\t{}".format(line[0], 1)

	# it's patent id    info
	else:
		# patent id    info
		print "{}\t{}".format(line[0], line[1])
