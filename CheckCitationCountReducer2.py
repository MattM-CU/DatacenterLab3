#!/usr/bin/env python
import sys
import string

last_pat_id = None
cur_citing_state = None

# patent id    -    state
# or
# citing id    cited id    state

for line in sys.stdin:

    line = line.strip()
    patent_id, cited_or_hyph, state = line.split('\t')

    # it's patent info -- this should always come before citations b/c of sorting
    if cited_or_hyph == '-':
        last_pat_id = patent_id
        cur_citing_state = state
    # it's a citation where the previous patent info is for the citing patent
    elif patent_id == last_pat_id:
        # citing id    citing state    cited id    cited state
        print '%s\t%s\t%s\t%s' % (patent_id, cur_citing_state, cited_or_hyph, state)

