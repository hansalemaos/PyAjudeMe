from group_and_iter_everything import (
groupby_is_integer
)
seq = ['sdsdsss',0.0, 2.0, 1, 1,
       3, 5, 3.0, 3.4,
       2.4, 25.3]

res = groupby_is_integer(
    seq=seq,
       continue_on_exceptions=True
)

from pprint import pprint
pprint(seq,width=1)
print('----------------')
pprint(res,width=1)