#あくまでも練習用で作ったものです。
#使用する際は画像ファイルをバックアップをとるなど、対策をしてください。

import os
from os import listdir

path ='' #ここに番号を変えたいファイルのパスを入力。

list1 = [filename for filename in listdir(path) if not filename.startswith('.')] #.DS_store　を除くための処理

print(list1) #フォルダ名を確認
print(len(list1)) #フォルダ数を確認


j = 0

for all_data in list1:

    jp_name = list1[j]  #日本語名のフォルダj番目を取得
    print(jp_name)  #ちゃんと取得できているか確認

    path2 = os.path.join(path,jp_name) #日本語のフォルダ名とそのフォルダまでのパスを結合する。
    print("path2=" + path2)  #ちゃんとパスが通っているか確認

            #先ほど取得したフォルダ（写真が１２枚入っているフォルダ）の中のファイル（jpegの写真データそのもの）を取得する。
    list2 = [filename for filename in listdir(path2) if not filename.startswith('.')]

    print(list2) #ちゃんと取得できているか確認

    i = 1 #1からスタートする
    for file_name in list2:
        old_path = os.path.join(path2,file_name) #古いパス
        print("old_path="+ old_path) #パスを確認する

        new_name = str(i) + ".jpg" #名前を番号に変換する
        new_path = os.path.join(path2,new_name) #新しいパスを通す

        os.rename(old_path,new_path) #古いパスから新しいパスに書き換える
        i = i + 1
        print(new_path)

    j = j + 1

#実行結果がファイルの名前が番号のみになっていれば成功です。
