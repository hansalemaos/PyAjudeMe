

from a_pandas_ex_apply_ignore_exceptions import(
pd_add_apply_ignore_exceptions
)
import pandas as pd
pd_add_apply_ignore_exceptions()

data = {
    'n1':[1,2,3],
    'n2':[0,4,'bad']

}
df=pd.DataFrame(data)
print(df.ds_apply_ignore(
    'deu ruim', # valor quando tem Exception
    lambda x:(
        x['n1'] / x['n2']
    ),axis=1
))