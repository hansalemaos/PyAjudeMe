import random, keyboard
import pandas as pd
from PrettyColorPrinter import  add_printer
add_printer(True)
from rapidfuzz import fuzz,process
import undetected_chromedriver as uc
from a_selenium2df import get_df
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def gdf(quer='*'):
    return get_df(driver,
                  By,
                  WebDriverWait,
                  expected_conditions,
                  queryselector=quer, with_methods=True, )


def fill_all():
    df=gdf()
    df2.cats=df2.cats.str.lower()
    letter = df.loc[df.aa_classList == 'ctLetter'].aa_innerText.iloc[0]
    needtofind = df.loc[df.aa_innerText.str.contains(
        '^((?:FILL THE BLANKS)|(?:PREENCHA OS CAMPOS))\n',
            na=False) & (df.aa_tagName == 'DIV') & (
        df.aa_classList == 'content')].aa_innerText.iloc[0].splitlines()[1:-1]
    choices = df2.cats.to_list()#.str.lower()
    goodcats = []
    for word in needtofind:
        rea = process.extract(word.lower(), choices, scorer=fuzz.WRatio, limit=1)
        goodcats.append((word, rea[0][0]))
    inputelements = df.loc[df.aa_localName == 'input'].dropna(subset='aa_tabIndex')

    for i, g in enumerate(goodcats):
        iele = inputelements.iloc[i]
        sendkeysvar = (random.choice([str(_).strip()
                                      for _ in df2.loc[df2.cats == g[-1],
                                            letter].iloc[0].split('|')]))

        iele.se_send_keys(sendkeysvar)

keyboard.add_hotkey('ctrl+alt+k', fill_all)
if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://stopots.com/14765')
    df2 = pd.read_excel(r"C:\stoppronto.xlsx")





























