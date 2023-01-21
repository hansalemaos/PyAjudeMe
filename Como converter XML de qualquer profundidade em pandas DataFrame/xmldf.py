from a_pandas_ex_xml2df import (
pd_add_read_xml_files
)
import pandas as pd
pd_add_read_xml_files()
df=pd.Q_Xml2df('https://gist.githubusercontent.com/jasonbaldridge/2597611/raw/c2c6a072c7d018c35aefad6b4739ac75247e5d92/music.xml')
print(df.to_string())