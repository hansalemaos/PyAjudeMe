# pip install a-selenium2df
# pip install undetected-chromedriver
# pip install PrettyColorPrinter
# pip install requests
# pip install keyboard
# pip install bs4
# pip install lxml
# pip install openpyxl
# pip install kthread
# pip install ujson
# pip install group-and-iter-everything
# pip install unidecode
# 
# 
# pip install rapidfuzz # se der 
# pip install thefuzz # se rapidfuzz não der 

import requests
import pandas as pd
from PrettyColorPrinter import add_printer
import bs4
add_printer(True)
link='https://www.dicionariopopular.com/adedonha-temas-respostas-stop'
resp = requests.get(
link)
df=pd.read_html(resp.content)
df2 = (
    pd.concat([x.set_index('LETRA').T for x
     in df if len(x) ==26],ignore_index=True)
)
soup=bs4.BeautifulSoup(resp.content, 'lxml')
i=[_.text for _ in soup.find_all('h2') if '. ' in str(_)]
df.insert(0, "cats", i)
df.cats=df.cats.str.split('. ',regex=False).str[-1]









