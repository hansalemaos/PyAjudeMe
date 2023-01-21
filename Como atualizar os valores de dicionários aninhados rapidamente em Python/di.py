d = {
    "level1": {
        "t1": {
            "s1": {"col1": 5, "col2": 4,
                   "col3": 4, "col4": 9},
            "s2": {"col1": 1, "col2": 5,
                   "col3": 4, "col4": 8},
            "s3": {"col1": 11, "col2": 8,
                   "col3": 2, "col4": 9},
            "s4": {"col1": 5, "col2": 4,
                   "col3": 4, "col4": 9},
        },
    },
    "level2": {
        "t1": {
            "s1": {"col1": 5, "col2": 4,
                   "col3": 4, "col4": 9},
            "s2": {"col1": 1, "col2": 5,
                   "col3": 4, "col4": 8},
            "s3": {"col1": 11, "col2": 8,
                   "col3": 2, "col4": 9},
            "s4": {"col1": 5, "col2": 4,
                   "col3": 4, "col4": 9},
        },
    },
}

from nestednop import (
NestedNop
)

nest = NestedNop(d)
for key, item in (nest
        .iterable_flat.items()):
    if (item['get_value']()>4
    and key[-1] == 'col1'
    and key[0] == 'level1'
    ):
        item['set_value'](10000)
print(nest.get_updated_iterable())
