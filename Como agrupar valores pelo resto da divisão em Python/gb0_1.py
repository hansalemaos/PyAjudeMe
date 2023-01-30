
from group_and_iter_everything import (
groupby_division_remainder
)

seq = [1, 5, 4, 44.44,
      22.22,33,31,2,3.3]

res = groupby_division_remainder(
      div=2,
      seq=seq,
      continue_on_exceptions=True,
      withindex=False,
      withvalue=True
)

from pprint import pprint
pprint(seq,width=1)
print('----------')
pprint(res)