import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


df = pd.read_csv('out.csv', header=None, names = ['翻刻文'])
print(df)
print(df.iat[0,0])
print(df.iat[1,0])
print(df.shape[0])

"""
options = Options()
# options.add_argument('--headless')

driver = webdriver.Firefox(firefox_options = options)
driver.get('https://google.com')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "q")))

search_bar = driver.find_element_by_name('q')
search_bar.send_keys('test')

search_bar.submit()
driver.implicitly_wait(30)

print(driver.current_url)
"""
