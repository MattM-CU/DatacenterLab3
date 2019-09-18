#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# split the line into CSV fields

	line = line.strip()

	words = line.split(',')

	if len(words) == 2:
		#
		# It's a citation
		#
		try:
			# make sure it's not the header
			cite = int(words[0])
			# use index 1 b/c cited is the 'key'
			# print('%s\t%s' % (words[1], ))
			# print(",".join(words))

			# citing id    C-cited id
			print "{}\tC-{}".format(words[0], words[1])
		except Exception as e:
			# improperly formed citation number
			# print("Exception ", e)
			continue
	else:
		#
		# It's patent info
		#
		try:
			# make sure it's not the header
			cite = int(words[0])

			# only care about patent info that has a state associated with it
			if words[5] and words[5] != '""':
				# patent id    S-state
				print "{}\tS-{}".format(words[0], words[5])
				# patent id    info
				print "{}\t{}".format(words[0], ",".join(words[1:]))
		except Exception as e:
			# improperly formed citation number
			# print("Exception ", e)
			continue

