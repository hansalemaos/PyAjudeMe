d={'k1': {'k2': {'k3': 5}}}

# padrão para acessar values
print(d['k1']['k2']['k3'])

# e quando os keys estão
# numa lista? Como acessar?
keys = ['k1','k2','k3']

import operator
from functools import reduce

reduce(operator.getitem,
       keys[:-1],
       d)[keys[-1]] =3332232

print(
reduce(operator.getitem,
       keys,d)
)
