def main():
    # 参照n文字辞書
    folder = 'character_dict'
    publish = '諸御趣意書并御下知向之写'
    
    for num in range(1, 33):
        # 現在の場所 ~/websreping/ で実行
        in_path  = os.path.join(os.getcwd(), 'out', folder)
        in_file = str(num) + 'words_' + publish + '.csv'

        

    return 0

main()
