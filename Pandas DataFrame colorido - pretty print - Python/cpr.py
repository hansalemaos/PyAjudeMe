csv = ("https://github.com/"
       "pandas-dev/pandas/raw/"
       "main/doc/data/titanic.csv")
import pandas as pd
from PrettyColorPrinter import (
add_printer
)
add_printer(True)
df=pd.read_csv(csv)
print(df)