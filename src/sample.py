import os
import pandas as pd

def main():
    folder = 'character_dict'
    publish = '諸御趣意書并御下知向之写'

    words = dict()
    nwords = dict()

    fin = 2

    for ndict in range(1,2):
        in_path = os.path.join(os.getcwd(), 'out', folder)
        in_file = str(ndict) + 'words_' + publish + '.csv'
        input = os.path.join(in_path, in_file)

        df = pd.read_csv(input, header=None, names=['n_dict'])

        for i, v in df.items():
            if v < 2:
                continue
            if i not in nwords.key():
                nwords[i] = v 

        

    return 0

main()
