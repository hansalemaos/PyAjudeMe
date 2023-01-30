
from group_and_iter_everything import (
groupby_substring
)
seq=['hallo', 'hacx', 'xahalcrw',
     'hatschi', 'boot', 'bobo']

res = (
groupby_substring(
    substring='hallo',
    seq=seq,
    withindex=True,
    withvalue=False
))

from pprint import pprint
pprint(seq, width=1)
print('------------')
pprint(res, width=1)