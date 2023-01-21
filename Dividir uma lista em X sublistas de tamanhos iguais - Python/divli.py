
def divli(l_,s,v=None,fill=False):
    l=[
        l_[i:i+s] for i in range(0,
                         len(l_),
                         s)
    ]
    _=([
        u for u in range(
            len(l[-2])-len(l[-1])
        ) if l[-1].append(v)
    ] if len(l) > 1 and fill
    else None)
    return l

li=[1, 2, 3, 4, 5, 6]

l0=divli(l_=li, s=4)
l1=divli(l_=li, s=4,
            v='X', fill=True)
l2=divli(l_=li, s=2,
            fill=False)
print(f'{l0=}')
print(f'{l1=}')
print(f'{l2=}')
