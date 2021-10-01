import os
import time
import pywinauto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint

def main():
    search_character = "line"

    for num in range(1, 5):
        img_path = r"C:\Users\kaay5\Documents\GitHub\WebScreiping\input\img"
        input_path = img_path + "\\" + search_character + "_" + str(num) + ".png"

        estimated_character = dict()
        published_character = dict()

        estimated_character, published_character = search_mojizo(input_path)
        print(estimated_character)

def search_mojizo(input_path = str()):
    estimated_character = dict()
    published_character = dict()
    try:    
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Firefox(firefox_options = options)

        url = 'https://mojizo.nabunken.go.jp/'
        driver.get(url)

        # 検索ワードを入力する場所が表示されるまで最大30秒待機する
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "search_img_area")))

        # アップロードボタンのエレメントを取得
        elements = driver.find_elements_by_id("search_img_area")
        element = elements[0]

        element.click()

        # pywinautoによる制御(titleはエクスプローラーの名前)
        findWindow = lambda: pywinauto.findwindows.find_windows(title=u'ファイルのアップロード')[0]

        dialog = pywinauto.timings.wait_until_passes(5, 1, findWindow)
        pwa_app = pywinauto.Application()
        pwa_app.connect(handle=dialog)
        window = pwa_app[u'ファイルのアップロード']
        window.wait('ready')

        #ファイル入力（Alt+N）
        file_path = input_path

        pywinauto.keyboard.send_keys("%N")
        edit = window.Edit4
        edit.set_focus()
        edit.set_text(file_path)

        # ダイアログの「開く」ボタンをクリック    
        button = window['開く(&O):']
        button.click()

        # MOJIZOの解析をクリック
        wait = WebDriverWait(driver, 20)
        driver.find_element_by_id("search_btn").location_once_scrolled_into_view
        elements = driver.find_elements_by_id("search_btn")
        element = elements[0]
        wait.until(EC.invisibility_of_element_located((By.XPATH,"//div[@class='blockUI blockOverlay']")))
        element.click()

        # elements = driver.find_elements_by_class_name("search_result_tbl")
        # print(elements)

        # 検索ワードを入力する場所が表示されるまで最大30秒待機する
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "search_result_tbl")))

        # テーブル内容取得
        tableElem = driver.find_element_by_class_name("search_result_tbl")
        trs = tableElem.find_elements(By.TAG_NAME, "tr")
        
        # ヘッダ行は除いて取得
        for i in range(1,len(trs)):
            tds = trs[i].find_elements(By.TAG_NAME, "td")
            line = ""
            for j in range(0,len(tds)-1):
                if i == 1:
                    estimated_character[j+1] = tds[j].text
                else:
                    published_character[j+1] = tds[j].text
        
        return estimated_character, published_character

    finally:
        if driver is not None:
            driver.quit()

main()
