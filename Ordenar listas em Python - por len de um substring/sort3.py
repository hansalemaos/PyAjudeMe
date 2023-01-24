l = ["hallo",
     "12hal33",
     "42ha004942r",
     "4204h213",
     "hall000",
     "h",
     "cvwsA"]

import re
sort_substr_len = lambda v,stri:(
sorted(
     v,key=lambda x: len(
          sorted(g, key=lambda i:
          len(i))[-1]
     ) if (g:=re.findall("|".join(
          [re.escape(stri[:_+1]) for
           _ in reversed(range(
               len(stri)
          ))]
     ),x)) else 0))

for _ in sort_substr_len(l, 'hallo'):
     print(_)