import ujson
import pandas as pd
from PrettyColorPrinter import add_printer
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from group_and_iter_everything import groupby_first_item
from unidecode import unidecode

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
print(allwa)

