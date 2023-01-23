people = {
    1: {"name": "John", "age": "27",
        "sex": "Male"},
    2: {"name": "Marie", "age": "22",
        "sex": "Female"},
    3: {"name": "Luna", "age": "24",
        "sex": "Female",
        "married": "No"},
    4: {"name": "Peter", "age": "29",
        "sex": "Male",
        "married": "Yes"},
}
from any_iter_to_html_table import (
create_html_table_from_iterable
)
import os
d = create_html_table_from_iterable(
    people,filename='f.html',
    title='bonito',sparsify=True
)
os.startfile('f.html')