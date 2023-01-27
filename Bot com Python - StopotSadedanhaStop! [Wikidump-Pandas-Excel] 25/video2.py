import ujson
import pandas as pd
from PrettyColorPrinter import add_printer
from flatten_any_dict_iterable_or_whatsoever import fla_tu


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

        



