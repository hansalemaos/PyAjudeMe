from group_and_iter_everything import iter_nested

li = [
    [
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
        ],
        [
            [21, 22, 23, 24],
            [
                25,
                26,
                27,
                28,
            ],
            [29, 30, 31, 32],
            [33, 34, 35, 36],
            [37, 38, 39, 40],
        ],
    ]
]


for l0, l1, l2, l3 in iter_nested(li):
    print(f"{l0=}")
    print(f"{l1=}")
    print(f"{l2=}")
    print(f"{l3=}")
    print("-----")

for l0 in li:
    for l1 in l0:
        for l2 in l1:
            for l3 in l2:
                print(f"{l0=}")
                print(f"{l1=}")
                print(f"{l2=}")
                print(f"{l3=}")
                print("-----")
