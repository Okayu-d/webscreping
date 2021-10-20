import os
import pandas as pd

def search_character(input_file_path: str(), character_dict: dict()):
    # ページの読み込み
    df = pd.read_csv(input_file_path, header=None, names = ['翻刻文'])
    
    # 一文を取得    
    for line in df['翻刻文']:
        # 一文字を取得
        for character in line:
            if character not in character_dict.keys():
                character_dict[character] = 1
            else:
                character_count = character_dict[character]
                character_count = character_count + 1
                character_dict[character] = character_count
    return character_dict    

def output_csv(character_dict: dict(), publish: str()):
    characters = int()
    for count in character_dict.values():
        characters = characters + count
    print(characters)

    # 出力ファイルの作成
    df = (pd.io.json.json_normalize(character_dict)).T
    df = df.set_axis(['count('+str(characters)+')'], axis='columns')

    # 出力path
    output_path = os.path.join(os.getcwd(), 'out', 'character_dict')
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    df.to_csv(os.path.join(output_path, publish + '.csv'))

    return 0


def main():
    # 参考文献になんの文字があるか，頻出文字，総文字数
    folder = "publish"
    publish = "諸御趣意書并御下知向之写"

    # 既出辞書
    character_dict = dict()

    # 参考文献のページ数
    for num in range(1, 194):
        # 現在の場所 + out + folder + 参考文献名(publish)
        input_page = os.path.join(os.getcwd(), 'out', folder, publish)
        file_name = "page_" + str(num) + ".csv"
        input_file_path = os.path.join(input_page, file_name)

        # 出現する文字
        character_dict = search_character(input_file_path, character_dict)
    
    output_csv(character_dict, publish)

main()
