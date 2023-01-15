import pandas as pd

# https://github.com/hansalemaos/a_pandas_ex_memorydump_to_df
# READ THE INSTRUCTIONS BEFORE INSTALLING!
# YOU PROBABLY NEED TO PATCH winappdbg
# https://github.com/hansalemaos/a_pandas_ex_memorydump_to_df/blob/main/winappdbg.zip
from a_pandas_ex_memorydump_to_df import pd_add_memorydf

pd_add_memorydf()

# pip install PrettyColorPrinter
from PrettyColorPrinter import add_printer  # colored DataFrame

add_printer(True)


df = pd.Q_df_from_memory(
    pid=15132,  # Open TaskManager
    # Download ProcDump: https://learn.microsoft.com/en-us/sysinternals/downloads/procdump
    procdumppath=r"C:\Program Files\procdump.exe",
    with_utf8_bytes=False,
)  # with_utf8_bytes=True takes much more time!


# Locating the username (be careful: might be in 2 or more lines)
df.loc[df.aa_ascii_str_all.str.contains("CROMAGS")]

# The index (4065095) is probably (99.9999999999%) different on your PC
df.ds_color_print_context(4065095)
