from group_and_iter_everything import (
groupby_startswith
)

seq=['hallo','baden', 'bonnot','bonita',
    'baba','bdoo', 'flaoti', 'fxa',
    'hanama' ]
res = groupby_startswith(
    n=3, seq=seq,
    continue_on_exceptions=True,
    withindex=True,
    withvalue=False

)

from pprint import pprint
pprint(seq,width=1)
print('--------------')
pprint(res,width=1)