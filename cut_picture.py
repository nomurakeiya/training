#画像を任意の大きさでトリミングできます


import os
from os import listdir
import cv2
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

path =''  #ここに番号を変えたいファイルのパスを入力。
#.DS_store　を除くための処理
list1 = [filename for filename in listdir(path) if not filename.startswith('.')]
print("list1=" )
print(list1)
print(len(list1))
j = 0
for all_data in list1:
    folder_name = list1[j] #英語名のフォルダi番目を取得
    print("foldername=" )
    print(folder_name)
    path2 = os.path.join(path,folder_name) #英語のフォルダ名とそのフォルダまでのパスを結合する。
    print("path2=")
    print(path2)
    list2 = [filename for filename in listdir(path2) if not filename.startswith('.')]
     #先ほど取得したフォルダ（写真が１２枚入っているフォルダ）の中のファイル（jpegの写真データそのもの）を取得する。
    print(list2)
    print(len(list2))
    i = 1
    for file_name in list2:
        path3 = os.path.join(path2,file_name) #画像までのパスを取得
        print("path3=")
        print(path3)
        img = cv2.imread(path3) #画像の読み込み(0を付けるとグレイスケールにもなる。)
        cv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #(opencvの)BGR画像を(matplotlibで使う)RGB画像に変換することで正しい色になる。
        fig2 = plt.figure(figsize=(16, 10)) #トリミング後の figureオブジェクト作成
        cropped = cv_img[300:900,350:1200]  #座標を使ってトリミング img[y:y+h, x:x+w] ここの値でトリミングする範囲を決まる
        ax2 = fig2.add_subplot(1, 1, 1)  #トリミング後の画像を表示  #fig全体に表示するので1行一列1番目
        ax2.set_title([j]) #グラフに名前を付ける
        plt.imshow(cropped) #トリミング後の画像
        plt.tight_layout() #グラフの空白を自動で調整
        filename = path3 #上書き保存なのでパスは読み込んだそのままを使う
        plt.savefig(filename) #保存する
        plt.close() #保存した後に、figureを表示しない
        i = i + 1

    j = j+1
