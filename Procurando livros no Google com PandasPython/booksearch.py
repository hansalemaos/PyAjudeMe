from a_pandas_ex_google_book_search_to_df import pd_add_google_books_search

# pip install a-pandas-ex-google-book-search-to-df

import pandas as pd
from PrettyColorPrinter import add_printer

add_printer(True)  # optional
pd_add_google_books_search()
df = pd.Q_search_for_books(
    search="Shakespeare",
    onestring=True,
    onlyfree=True,
    add_to_search_query="",
    language="en",
    timeout=15,
)
print(df)
