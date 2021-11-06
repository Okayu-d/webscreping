import os
import pandas as pd
import pprint

def read_dict(in_path: str(), in_file: str(), in_dict_num: int()):
    # output_dict
    out_dict = dict()
    # input_dict_path
    input = os.path.join(in_path, in_file)
    df = pd.read_csv(input, index_col=0)
    # csv -> dict
    for i in range(0, len(df)):
        key = df.index[i]
        val = df.at[key, df.columns[0]]
        if val < 4:
            continue
        if key not in out_dict.keys():
            out_dict[key] = val
        else:
            continue
    return out_dict

def exist_dict(d1: dict(), d2: dict()):
    # dict1, dict2 are compered -> exist_num of dict is higher than other dict, exist
    # len_value d1 > d2

    d2_keys = list(d2.keys())
    d2_values = list(d2.values())

    for k, v in d1.items():
        for index, key in enumerate(d2_keys):
            if len(key) >= len(k):
                continue
            if key in k:
                if v >= d2_values[index]:
                    d2_keys.pop(index)
                    d2_values.pop(index)
                    d2_keys.append(k)
                    d2_values.append(v)

    out_d = dict(zip(d2_keys, d2_values))
    
    return out_d

def output_csv(character_dict: dict(), publish: str()):
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
    df.to_csv(os.path.join(output_path, 'dictionary_words_' + publish + '.csv'))

def main():
    input_words_len = 2
    folder = 'character_dict'
    publish = '諸御趣意書并御下知向之写'
    in_path = os.path.join(os.getcwd(), 'out', folder)

    op_dict = dict()
    dm_dict = dict()

    for ndict in range(input_words_len, len(os.listdir(in_path))+1):
        # input path, file, ndict
        in_file = str(ndict) + 'words_' + publish + '.csv'
        # read
        dm_dict = read_dict(in_path, in_file, ndict)
        # op_dict initialize
        if ndict == input_words_len:
            op_dict = dm_dict
            continue

        # prevet zize0
        if len(dm_dict) == 0:
            continue

        op_dict = exist_dict(dm_dict, op_dict)
        
    output_csv(op_dict, publish)
        
    return 0

main()
# test()