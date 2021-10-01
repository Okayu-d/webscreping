import os
import time
import csv
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

def search_beaf(path = str(), search_character = str(), line_character = list(), \
    search_b2 = dict(), search_b1 = dict(), search_a1 = dict(), search_a2 = dict()):

    # 本文の読み込み
    df = pd.read_csv(path, header=None, names = ['翻刻文'])

    for line in df['翻刻文']:
        # 特定の文字が行に含まれているかどうか
        if search_character in line:
            line_character.append(line)
            line_list = list(line)
            search_index = line.find(search_character)
            # print(line_list, line_list[search_index])
        else:
            continue

        line_range = len(line_list)
        # 検索の一つ前の文字
        before_after = 1
        if can_add_dictionary(line_range, search_index - before_after):
            apper_character = line_list[search_index - before_after]
            search_b1 = add_dictionary(apper_character, search_b1)
        # 検索の二つ前の文字
        before_after = 2
        if can_add_dictionary(line_range, search_index - before_after):
            apper_character = line_list[search_index - before_after]
            search_b2 = add_dictionary(apper_character, search_b2)
        # 検索の一つ後の文字
        before_after = 1
        if can_add_dictionary(line_range, search_index + before_after):
            apper_character = line_list[search_index + before_after]
            search_a1 = add_dictionary(apper_character, search_a1)
        # 検索の二つ後の文字
        before_after = 2
        if can_add_dictionary(line_range, search_index + before_after):
            apper_character = line_list[search_index + before_after]
            search_a2 = add_dictionary(apper_character, search_a2)

    return line_character, search_b2, search_b1, search_a1, search_a2


def main():
    now_path = os.getcwd()
    # 探す文字
    search_character = '々'
    folder = "publish"
    publish = "諸御趣意書并御下知向之写"


    # 探した文字を入れるリスト
    line_character = list()
    d_b2 = dict()
    d_b1 = dict()
    d_a1 = dict()
    d_a2 = dict()

    # for文で全ての文を検索
    for num in range(1, 194):
        # output_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.getcwd()
        output_dir = os.path.join(output_dir, 'out', folder, publish)

        file_name = "page_" + str(num) + ".csv"
        output_file = os.path.join(output_dir, file_name)

        # 前後の文字を検索
        line_character, d_b2, d_b1, d_a1, d_a2 = search_beaf(output_file, search_character, line_character, d_b2, d_b1, d_a1, d_a2)
    
    pprint.pprint(line_character)
    print(d_b2)
    print(d_b1)
    print(search_character)
    print(d_a1)
    print(d_a2)

    # output_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.getcwd()
    output_dir = os.path.join(output_dir, 'out', 'before_after')
    os.chdir(output_dir)
    if not os.path.exists(search_character):
        os.mkdir(search_character)
    os.chdir(now_path)
    output_dir = os.path.join(output_dir, search_character)
    file_name = search_character + '_b2' + ".csv"
    output_file = os.path.join(output_dir, file_name)

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in d_b2.items():
            writer.writerow([k, v])
    f.close

    os.chdir(now_path)

    output_dir = os.getcwd()
    output_dir = os.path.join(output_dir, 'out', 'before_after')
    os.chdir(output_dir)
    if not os.path.exists(search_character):
        os.mkdir(search_character)
    os.chdir(now_path)
    output_dir = os.path.join(output_dir, search_character)

    file_name = search_character + '_b1' + ".csv"
    output_file = os.path.join(output_dir, file_name)

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in d_b1.items():
            writer.writerow([k, v])
    f.close

    os.chdir(now_path)
    output_dir = os.getcwd()
    output_dir = os.path.join(output_dir, 'out', 'before_after')
    os.chdir(output_dir)
    if not os.path.exists(search_character):
        os.mkdir(search_character)
    os.chdir(now_path)
    output_dir = os.path.join(output_dir, search_character)
    file_name = search_character + '_a1' + ".csv"
    output_file = os.path.join(output_dir, file_name)

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in d_a1.items():
            writer.writerow([k, v])
    f.close

    os.chdir(now_path)
    output_dir = os.getcwd()
    output_dir = os.path.join(output_dir, 'out', 'before_after')
    os.chdir(output_dir)
    if not os.path.exists(search_character):
        os.mkdir(search_character)
    os.chdir(now_path)
    output_dir = os.path.join(output_dir, search_character)
    file_name = search_character + '_a2' + ".csv"
    output_file = os.path.join(output_dir, file_name)

    with open(output_file, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in d_a2.items():
            writer.writerow([k, v])
    f.close




main()



