# .h5モデルでの新規画像結果出力　

# 　無分類フォルダを読み込み
# 　分類フォルダ生成
# 　分類結果によって対象フォルダに保存

import tensorflow as tf
from tensorflow import keras
import cv2
import time
#from keras.preprocessing.image import array_to_img, img_to_array, load_img
# Helper libraries
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
import shutil

# モデル読み込み
h5file = glob.glob(os.path.join("*.h5"))
if len(h5file) > 0:
    new_model = tf.keras.models.load_model(h5file[0], compile=False, custom_objects=None)
    h5name = h5file[0][:-3]
else:
    print("モデルがありません")

print("h5 file is : ", h5name)
# 分類後の画像を保存するディレクトリを生成
os.mkdir('分類済')
os.mkdir('分類済/A')
os.mkdir('分類済/B')
os.mkdir('分類済/C')
os.mkdir('分類済/D')

# zipファイル解凍
zipfile = glob.glob(os.path.join("*.zip"))
shutil.unpack_archive(zipfile[0], 'images')
# 解凍した画像の読み込み
images = glob.glob(os.path.join('/content/images' , '**/*.jpg'), recursive=True)
print(zipfile[0])
print("枚数：", len(images))

for i in range(1, len(images)):
    # for i in range(1000):
    img_src = cv2.imread(images[i], cv2.IMREAD_COLOR)  # `保存用画像

    img = tf.keras.utils.img_to_array(
        tf.keras.utils.load_img(images[i], grayscale=False, target_size=(128, 128)))  # 処理用画像  , interpolation = 'nearest'
    X = []
    X.append(img)
    X = np.asarray(img) / 255.0
    X = X.reshape(1, 128, 128, 3)

    predictions_real = new_model.predict(X)  # 学習データとの照合
    predicted_label = np.argmax(predictions_real)

    Score0 = (predictions_real * 100)
    if predicted_label == 0:
        image_path = '分類済/A/' + str(round(Score0[0, predicted_label], 0)) + "_"
        label = "   bad"
        cv2.imwrite(image_path + str(i) + "a.jpg", img_src)

    elif predicted_label == 1:
        image_path = '分類済/B/' + str(round(Score0[0, predicted_label], 0)) + "_"
        label = "  good"
        cv2.imwrite(image_path + str(i) + "b.jpg", img_src)
        
    elif predicted_label == 2:
        image_path = '分類済/C/' + str(round(Score0[0, predicted_label], 0)) + "_"
        label = "  good"
        cv2.imwrite(image_path + str(i) + "c.jpg", img_src)

    elif predicted_label == 4:
        image_path = '分類済/D/' + str(round(Score0[0, predicted_label], 0)) + "_"
        label = "double"
        cv2.imwrite(image_path + str(i) + "d.jpg", img_src)

    print(i, " ■Result: ", label, "  ■Probability: ", str(round(Score0[0, predicted_label], 1)), " %")

zipname = "分類済_" + zipfile[0][:-4] + "_by_" + h5name
shutil.make_archive(zipname, 'zip', root_dir='分類済')
print("Finish")
