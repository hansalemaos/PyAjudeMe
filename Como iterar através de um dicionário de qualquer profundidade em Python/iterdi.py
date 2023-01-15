# pip install group-and-iter-everything
from group_and_iter_everything import (
iter_nested_dict
)

d = {
    1: {
        2: {
            "IDs": {
                "BookID": ["543533254353",
                           "4324232342"],
                "SalesID": ["543267765345",
                            "4353543"],
                "StoreID": ["111111",
                            "1121111"],
            },
            "Name": "boring Tales of Dragon Slayers",
        },
        "IDs": {
            "BookID": ["543533254353"],
            "SalesID": ["543267765345"],
            "StoreID": ["123445452543"],
        },
        "Name": "Thrilling Tales of Dragon Slayers",
    }
}
for keys,item in iter_nested_dict(d):
    print(f'{keys}   ->     {item}')



'output:'
# (1, 2, 'IDs', 'BookID', 0)  > 543533254353
# (1, 2, 'IDs', 'BookID', 1)  > 4324232342
# (1, 2, 'IDs', 'SalesID', 0) > 543267765345
# (1, 2, 'IDs', 'SalesID', 1) > 4353543
# (1, 2, 'IDs', 'StoreID', 0) > 111111
# (1, 2, 'IDs', 'StoreID', 1) > 1121111
# (1, 2, 'Name')              > boring Tales of Dragon Slayers
# (1, 'IDs', 'BookID', 0)     > 543533254353
# (1, 'IDs', 'SalesID', 0)    > 543267765345
# (1, 'IDs', 'StoreID', 0)    > 123445452543
# (1, 'Name')                 > Thrilling Tales of Dragon Slayers





