from collections import (
defaultdict
)
nd = lambda : (
    defaultdict(nd)
)
d = nd()
d['k1']['k2']['k3'] = 5
print(d['k1']['k2']['k3'])
