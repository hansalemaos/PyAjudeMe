from group_and_iter_everything import (
group_values_in_flattened_nested_iter_and_count
)

seq=[.1,.2,.3,.4,[.1,.2,.3,.4,.5,
    (.5,.5,.5,.5,[.1,.3,.4,[.3,.3,.4]])],
    {(.3,.4), (.1,.4)}]

res = group_values_in_flattened_nested_iter_and_count(
    seq=seq,
    withindex=True

)
from pprint import pprint
pprint(seq, width=1)
print('\n\n')
pprint(res , width=1)