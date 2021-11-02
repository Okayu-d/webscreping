import os
import pandas as pd

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
        if val == 1:
            continue
        if key not in out_dict.keys():
            out_dict[key] = val
        else:
            continue
    return out_dict

def main():
    folder = 'character_dict'
    publish = '諸御趣意書并御下知向之写'
    in_path = os.path.join(os.getcwd(), 'out', folder)

    op_dict = dict()
    dm_dict = dict()

    for ndict in range(1, len(os.listdir(in_path))+1):
        # input path, file, ndict
        in_file = str(ndict) + 'words_' + publish + '.csv'
        # read
        dictionaly = read_dict(in_path, in_file, ndict)
        if len(dictionaly) != 0:
            continue
        

            print(dictionaly)
    
    return 0

main()
