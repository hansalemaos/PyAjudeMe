l =[
    (1,2),
    (3,4),
    (4,5)
]

print(f'{l=}')
xy = [
    list(x)
    for x in zip(*l)
]
print(f'{xy=}')

orig = [
    x for x in iter(
        zip(*xy)
    )
]
print(f'{orig=}')