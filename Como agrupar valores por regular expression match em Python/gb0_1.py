
from group_and_iter_everything import (
groupby_regular_expression_matches
)
seq=[1, 'xx', '3', 5, 'AA',
     'BB', 22.22, 'AAAAA', '4324']
res=groupby_regular_expression_matches(
    regexpressions=[r'^\d+$', '^A+$'],
    seq=seq,
    continue_on_exceptions=True,
    withindex=True,
    withvalue=False


)
from pprint import pprint
pprint(seq,width=1)
print('---------')
pprint(res,width=1)

