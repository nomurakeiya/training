#日本語のフォルダ名を英語のフォルダ名に変えます。


from os import listdir
from googletrans import Translator

#フォルダ名を全て取得する
path = ''  #ここに番号を変えたいファイルのパスを入力。

#.DS_store　を除くための処理
list1 = [filename for filename in listdir(path) if not filename.startswith('.')]

#英語に変換する
translator = Translator() #入力する日本語は、上で取得した全フォルダ
jp_words = list1
en_words = []

for src in jp_words:
    dst = translator.translate(src, src='ja', dest='en')
    en_words.append(dst.text)
    i = 0


for file_name in list1:
    jp_name = list1[i] #日本語名のファイルi番目を取得
    print(jp_name)
    old_name = os.path.join(path,jp_name) #日本語のファイル名とそのファイルまでのパスを結合する。
    print(old_name)
    en_name = en_words[i] #英語名のファイルi番目を取得
    print(en_name)
    new_name = os.path.join(path,en_name)   #英語のファイル名とそのファイルまでのパスを結合する。
    print(new_name)
    os.rename(old_name,new_name)  #日本語名のパスを英語名のパスに変換する
    i = i + 1
