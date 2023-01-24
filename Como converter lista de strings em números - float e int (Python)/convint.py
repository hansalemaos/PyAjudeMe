test = [
"234.1.1.1", "++1", "--1",
"-1-1", "1.23e10e5", "211",
"-1", "+1", "0.0", ".1",
"1.2345", "-1.2345", "+1.2345",
"1.2345e10", "1.2345e-10",
"-1.2345e10", "-1.2345E10",
'babadx', None, [232, 43],
(34, 432, 5334)]

import re, ast
reg = re.compile(
    r'^[-.\de+]+',
    flags=re.I
)

def conv(x):
    try:
        if reg.search(x):
            return (
                ast.literal_eval(x)
            )
    except Exception:
        return x

for b in test:
    print(b,type(b),
          g:=conv(b), type(g))
