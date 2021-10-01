import os
import time
import pandas as pd
import pprint

def add_dictionary(apper_character = str(), d1 = dict()):
    # 新出文字の場合
    if  d1 == None or apper_character not in d1.keys():
        d1.setdefault(apper_character, '1')
    else:
        count_up = int(d1.get(apper_character)) + 1
        d1[apper_character] = str(count_up)
    return d1

def can_add_dictionary(line_range = int(), search_index = int()):
    # 検索範囲
    if 0 > search_index or search_index >= line_range:
        return False
    else:
        return True

def search_beaf(path = str(), search_character = str(), line_character = dict()):
    # 本文の読み込み
    df = pd.read_csv(path, header=None, names = ['翻刻文'])

    num = 0

    for line in df['翻刻文']:
        # 特定の文字が行に含まれているかどうか
        if search_character in line:
            num = num + 1
            path2 = path + '_' + str(num)
            line_list = list(line)
            search_index = line.find(search_character)
            line_character[path2] = line
        else:
            continue
    return line_character

def main():
    # 探す文字
    search_character = 'れ'
    folder = "publish"
    publish = "諸御趣意書并御下知向之写"

    # 探した文字を入れるリスト
    line_character = dict()
    # for文で全ての文を検索
    for num in range(1, 194):
        output_dir = os.getcwd()
        output_dir = os.path.join(output_dir, 'out', folder, publish)
        file_name = "page_" + str(num) + ".csv"
        output_file = os.path.join(output_dir, file_name)

        # 前後の文字を検索
        line_character = search_beaf(output_file, search_character, line_character)

    # ファイルの出力
    df = pd.io.json.json_normalize(line_character)
    df = df.T
    df = df.set_axis(['content'], axis = 'columns')

    output_path = os.path.join(os.getcwd(), 'out', 'character_line')

    df.to_csv(os.path.join(output_path, search_character + '.csv'))
    
main()



