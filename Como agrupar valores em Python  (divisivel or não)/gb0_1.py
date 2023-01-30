from group_and_iter_everything import (
groupby_can_be_divided_by
)

seq = ['1',1,3,4,5,6,7,22.22,42]
res = (
    groupby_can_be_divided_by(
        div=2,
        seq=seq,
        continue_on_exceptions=True,
        withindex=True,
        withvalue=False

    )
)

from pprint import pprint
pprint(res )