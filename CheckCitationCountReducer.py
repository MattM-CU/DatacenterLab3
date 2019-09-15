#!/usr/bin/env python
import sys
import string

last_pat_id = None
cur_state = None

# patent id    -    state
# or
# cited    citing    1

for line in sys.stdin:

    line = line.strip()
    patent_id, citing_or_state, state_or_1 = line.split('\t')

    # it's patent info -- this should always come before citations b/c of sorting
    if citing_or_state == '-':
        last_pat_id = patent_id
        cur_state = state_or_1
        # patent id    -    state
        print '%s\t%s\t%s' % (last_pat_id, '-', cur_state)
    # it's a citation for the previous patent
    elif patent_id == last_pat_id:
        # citing id    cited id    state
        print '%s\t%s\t%s' % (citing_or_state, patent_id, cur_state)

