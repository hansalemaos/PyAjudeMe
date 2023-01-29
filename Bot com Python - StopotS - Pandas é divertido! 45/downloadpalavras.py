import ujson
import pandas as pd
from PrettyColorPrinter import add_printer
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from group_and_iter_everything import groupby_first_item
from unidecode import unidecode
from string import ascii_lowercase

add_printer(True)
fi = r"F:\neuedownloads\kaikki_dot_org-dictionary-Portuguese-by-pos-noun.json"
with open(fi, mode='rb') as f:
    data = f.read()

allloaded = []
for cc in data.splitlines():
    allloaded.append(ujson.loads(cc))
df=pd.DataFrame(allloaded)

df['catsso'] = df.senses.apply(lambda x:[p[0] for p in (
    fla_tu(x)) if 'categories' in p[1]])

df = df.explode('catsso').reset_index(drop=True)
df=df.dropna(subset='catsso').reset_index(drop=True)
df.word = df.word.str.lower()
df.catsso=df.catsso.str.replace(r'^[^:]*:', '',regex=True)

allf = []
for name, group in df.groupby('catsso'):
    if len(group) > 20:
        l = [unidecode(x) for x in group.word.to_list()]
        dax= pd.DataFrame(groupby_first_item(l,
                           continue_on_exceptions=True,
                           withindex=False).items())
        dax['categ'] = name
        allf.append(dax.copy())

allwa = pd.concat(allf)
allwa=allwa.explode(1).drop_duplicates().reset_index(drop=True).rename(
    columns={0:'letter', 1:'words'}
)
print(allwa)

allnd = []
for name, group in allwa.groupby('categ'):
    oca=[]
    for le in ascii_lowercase:
        ga=group.loc[group['letter'] == le]
        ga2 = group.categ.iloc[0]
        if not ga.empty:
            ga1 = '|'.join(ga.words.to_list())

            oca.append((le,ga1,ga2))
        else:
            oca.append((le, '-', ga2))
    allnd.append(pd.DataFrame(oca.copy()).copy())

allnewca=[]
for i in allnd:
    daxs = i.set_index(0).T.copy()
    catss = pd.Series([daxs.iloc[1].iloc[0]])
    daxs = daxs.drop(2).reset_index(drop=True)
    daxs.insert(0, 'cats',catss)
    allnewca.append(daxs.copy())
df=pd.concat(allnewca, ignore_index=True)
df=df.loc[~df.cats.str.contains(r'^[\d\s]*$'
        )].reset_index(drop=True).fillna('-')

df.columns = [x.upper() if len(x) == 1 else x
              for x in df.columns ]

df2=pd.read_excel(r"C:\stopparavideo.xlsx")
df=pd.concat([df2,df],ignore_index=True)
df.to_excel('c:\\stoppronto.xlsx', index=False)




