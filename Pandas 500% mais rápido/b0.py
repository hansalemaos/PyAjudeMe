import pandas as pd
df = pd.read_csv("https://github.com"
                 "/pandas-dev"
                 "/pandas/raw/main"
                 "/doc/data/"
                 "titanic.csv")

# Criando um DataFrame com 891.000 rows
df = pd.concat([df.copy() for x
                   in range(1000)
                   ],ignore_index=True)
df = df.sample(
    len(df))

print(df)

pq=((df['PassengerId']/2.21 >= 150)
&(df['Fare']*10.4431 <= 80)
&(df['Survived']*134.41>0))

# %timeit pq=((df['PassengerId']/2.21 >= 150) &(df['Fare']*10.4431 <= 80) &(df['Survived']*134.41>0))

import numexpr
a,b,c=(df['PassengerId'].__array__(),
       df['Fare'].__array__() ,
       df['Survived'].__array__())
numexpr.evaluate('(a/2.21 >= 150) & (b*10.4431 <= 80) & (c*134.41>0)')
# %timeit numexpr.evaluate('(a/2.21 >= 150) & (b*10.4431 <= 80) & (c*134.41>0)')





















