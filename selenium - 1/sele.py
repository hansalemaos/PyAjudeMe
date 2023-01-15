import undetected_chromedriver as uc
from a_selenium2df import get_df
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
from PrettyColorPrinter import add_printer
add_printer(True)


if __name__ == '__main__':

    driver = uc.Chrome()
    driver.get(r"https://www.gmail.com")
	
	
	# alguns exemplos de pandas 
	# df = get_df(driver, By, WebDriverWait, expected_conditions, queryselector="*", with_methods=True, )

    # df.loc[df.aa_localName.str.contains('input', na=False) & df.aa_outerHTML.str.contains('type="email"')].iloc[
    #     0].se_send_keys('xxxxxxxxxxxx')

    # df.loc[df.aa_innerText.str.contains('Weiter', na=False) & df.aa_localName.str.contains('button', na=False)].iloc[
    #     0].se_click()

    # df = get_df(driver, By, WebDriverWait, expected_conditions, queryselector="input", with_methods=True, )
    # df.loc[df.aa_type.str.contains('password', na=False)].iloc[0].se_send_keys(pwd)

    # df = get_df(driver, By, WebDriverWait, expected_conditions, queryselector="button", with_methods=True, )

    # df.loc[df.aa_innerText.str.contains('Weiter', na=False)].iloc[0].se_click()