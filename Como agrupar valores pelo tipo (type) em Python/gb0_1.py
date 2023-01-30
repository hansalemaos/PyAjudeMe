
from group_and_iter_everything import (
groupby_type
)
seq=["dd", "b", "ff", "saaa",
    1, 3, 5, 22.22, (3, 4),
    [333, 4]]
res = (
    groupby_type(
        seq=seq
    )
)

from pprint import pprint
pprint(seq,width=1)
print('---------')
pprint(res,width=1)