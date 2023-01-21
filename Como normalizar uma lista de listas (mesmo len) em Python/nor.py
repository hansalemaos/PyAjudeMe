# temos:
l = [[1, 2, 3], [4, 5], [1]]

# queremos:
l1 = [[1, 2, 3], [4, 5, None], [1, None, None]]


def normalize_list(l, fillv=None):
    ml = max([len(x) for x in l])
    nl = []
    [x for x in l if (nl.append(((x + ([fillv] * (ml - len(x)))))))]
    return nl


print(normalize_list(l, fillv=None))
