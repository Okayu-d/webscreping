import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
seeting = 0

def main():
    # name = "諸御趣意書并御下知向之写"
    # url = 'https://honkoku.org/app/#/transcription/3344C7DFC5C6AB5DF0FD5FAFBDDD934C/'
    name = '(養生教訓)医者談義 5巻'
    url = 'https://honkoku.org/app/#/transcription/177155A90C3474B9F8EB3E390312F3A5/'

    fin_page = 101
    search_minna(name, url, fin_page)

def search_minna(name = str(), url = str(), fin_page = int()):
    now_path = os.getcwd()
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(firefox_options = options)
    
    # os.chdir('../')

    for i in range(5, fin_page):

        urls = url + str(i) + '/'
        driver.get(urls)

        # 検索ワードを入力する場所が表示されるまで最大30秒待機する
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "koji")))

        if setting == 1:
            span_remove = driver.find_elements_by_class_name('furigana-right')
            for j, k in enumerate(span_remove):
                test = driver.execute_script('arguments[0].remove()', span_remove[j])

        content = driver.find_element_by_class_name("koji")
        
        # 実行ファイルの絶対パスを取得し、そのファイルパスのディレクトリパスを取得する
        output_dir = str(os.getcwd())
        output_dir = os.path.join(output_dir, 'out', 'publish', name)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        file_name = "page_" + str(i) + ".csv"

        # output_dirとfile_nameを結合したパスを作成する
        output_file = os.path.join(output_dir, file_name)

        with open(output_file, mode='w', encoding='utf-8') as f:
            f.write(content.text)
        f.close()

    os.chdir(now_path)
        
main()
