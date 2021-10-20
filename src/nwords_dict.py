import os
import pandas as pd
import ast

def word_dict(input_file_path: str(), n_dict: dict(), max_len: int()):
    # n文字列対応の辞書 'n': words → 'words' : count
    # ページの読み込み
    df = pd.read_csv(input_file_path, header=None, names=['翻刻文'])

    # 一文を取得
    for line in df['翻刻文']:
        line_len = len(line)
        if max_len < line_len:
            max_len = line_len

        #取得文字数
        for n in range(1, line_len+1):
            # print(line, n)
            # 文字列の番地
            if n not in n_dict.keys():
                n_dict[n] = dict()
            for i in range(0, line_len):
                if i+(n-1) < line_len:
                    word_dict = n_dict[n]
                    words = join_char(i, n, line)
                    if words not in word_dict.keys():
                        word_dict[words] = 1
                    else:
                        words_count = word_dict[words]
                        words_count = words_count + 1
                        word_dict[words] = words_count
                    # print(n_dict[n], word_dict)
                    n_dict[n] = word_dict
                else:
                    break

    return n_dict, max_len

def join_char(start_num: int(), chatch_num: int(), line: str()):
    words = line[start_num]
    for i in range(start_num+1, start_num+chatch_num):
        words = words + line[i]
    return words

def output_csv(character_dict: dict(), publish: str(), words: int()):
    characters = int()
    for count in character_dict.values():
        characters = characters + count
    # print(characters)

    # 出力ファイルの作成
    df = (pd.io.json.json_normalize(character_dict)).T
    df = df.set_axis(['count('+str(characters)+')'], axis='columns')

    # 出力path
    output_path = os.path.join(os.getcwd(), 'out', 'character_dict')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    df.to_csv(os.path.join(output_path, str(words) + 'words_' + publish + '.csv'))

    return 0

def run():
    # 参考文献になんの文字があるか，頻出文字，総文字数
    folder = "publish"
    publish = "諸御趣意書并御下知向之写"

    # 最大の文字列の長さ
    max_len = int(0)

    # 既出辞書
    character_dict = dict()

    # 出力用変数
    output_dict = dict()

    # 参考文献のページ数
    for num in range(1, 194):
        # 現在の場所 + out + folder + 参考文献名(publish)
        input_page = os.path.join(os.getcwd(), 'out', folder, publish)
        file_name = "page_" + str(num) + ".csv"
        input_file_path = os.path.join(input_page, file_name)

        # 出現する文字
        character_dict, max_len = word_dict(input_file_path, character_dict, max_len)

        # 消す
        # break
    
    for i in range(1, max_len-1):
        if i not in character_dict.keys():
            continue
        output_dict = character_dict[i]
        output_csv(output_dict, publish, i)
        
def main():
    run()

main()
