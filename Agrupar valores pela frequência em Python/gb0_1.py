from group_and_iter_everything import (
groupby_frequency
)

seq=[ "dd", "b", "ff", "saaa",
      1, 3, 3, 3, 5, "b", 3, 5,
      22.22, (3, 4), [333, 4], ]

res = (groupby_frequency(
    seq=seq,
    withindex=True,
    withvalue=False


))
from pprint import pprint
pprint(seq,width=1)
print('-------------')
pprint(res,width=1)