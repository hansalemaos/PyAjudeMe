import pandas as pd
from a_pandas_ex_image_tools import pd_add_image_tools

pd_add_image_tools()
df = pd.Q_image2df(
    r"https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
)
df.loc[
    (df.red > 200) & (df.green > 200) & (df.blue < 120), ["red", "green", "blue"]
] = [0, 255, 0]

df.loc[(df.x % 10 == 0), ["red", "green", "blue"]] = [0, 0, 0]

df.loc[(df.y % 50 == 0), ["red", "green", "blue"]] = [255, 0, 0]

df.loc[
    (df.red > 200) & (df.green > 200) & (df.blue > 200), ["red", "green", "blue"]
] = [255, 0, 255]

df.im_show_df_image()
