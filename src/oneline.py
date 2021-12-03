
def main():
    # 参考文献になんの文字があるか，頻出文字，総文字数
    folder = "publish"
    publish = "(養生教訓)医者談義 5巻"

    for page in range(start, fin):
        

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