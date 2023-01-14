import pandas as pd
import requests, bs4
resp = requests.get(
    'https://www.dicionariopopular.com/adedonha-temas-respostas-stop'
)
df=pd.concat(
    [x.set_index('LETRA').T
     for x in
     pd.read_html(resp.content)
     if len(x) == 26 #alfabeto A-Z
     ], ignore_index=True
)
soup=bs4.BeautifulSoup(
    resp.content,'lxml'
)
df.index = [
    x.text for x in
    soup.find_all('h2')
    if '. ' in str(x)
]
df.to_excel('c:\\stoplista.xlsx')