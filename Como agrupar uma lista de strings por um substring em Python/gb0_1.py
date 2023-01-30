from group_and_iter_everything import (
groupby_first_occurrence_in_string
)

seq = ['as', 'hallo', 'boot',
       'baba', 'bdoo', 'flaot',
       'hmama']

res =(
groupby_first_occurrence_in_string(
    char='a',
    seq=seq,
    withindex=True,
    withvalue=False
))

from pprint import pprint
pprint(seq,width=1)
print('------------')
pprint(res,width=1)