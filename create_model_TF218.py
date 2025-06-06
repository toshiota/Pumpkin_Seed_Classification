# TensorFlow and tf.keras
#かぼちゃの種分類用に、A,A,C,D（重なり）の4種類に分類する。
#ZIP内には、ABCD
# TensorFlow and tf.keras
import tensorflow as tf

from sklearn.model_selection import train_test_split
#from tensorflow.keras.utils.image import array_to_img, img_to_array, load_img

#import  Helper libraries
import numpy as np
import cv2
import requests
import glob
import os
import time
import datetime
import PIL

import shutil

print(tf.__version__)
print(tf.test.gpu_device_name())
now = datetime.datetime.now()+ datetime.timedelta(hours=9)

#zipファイル解凍
zipfile=glob.glob(os.path.join("*.zip"))
shutil.unpack_archive(zipfile[0], 'images')
#解凍した画像の読み込み


X = []
Y = []

# Aの画像#
images0 = glob.glob(os.path.join('/content/images/A', "*.jpg"))
targetsize=(128,128)
print(len(images0))
for i in range(len(images0)):
    img = tf.keras.utils.img_to_array((tf.keras.utils.load_img(images0[i], color_mode='rgb', target_size=targetsize)))
    img2 = cv2.flip(img, 0)
    img3 = cv2.flip(img, 1)
    img4 = cv2.flip(img, 2)
    img5 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img6 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    img7 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)
    img8 = cv2.rotate(img4, cv2.ROTATE_90_CLOCKWISE)
    X.append(tf.keras.utils.img_to_array(img))
    X.append(tf.keras.utils.img_to_array(img2))
    X.append(tf.keras.utils.img_to_array(img3))
    X.append(tf.keras.utils.img_to_array(img4))
    X.append(tf.keras.utils.img_to_array(img5))
    X.append(tf.keras.utils.img_to_array(img6))
    X.append(tf.keras.utils.img_to_array(img7))
    X.append(tf.keras.utils.img_to_array(img8))
    Y.extend([0, 0, 0, 0, 0, 0, 0, 0])
print("1/4 A Load" ,i,  len(X))

# Bの画像
images1 = glob.glob(os.path.join('/content/images/B', "*.jpg"))
for i in range(len(images1)):
    img = tf.keras.utils.img_to_array((tf.keras.utils.load_img(images1[i], color_mode='rgb', target_size=targetsize)))
    img2 = cv2.flip(img, 0)
    img3 = cv2.flip(img, 1)
    img4 = cv2.flip(img, 2)
    img5 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img6 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    img7 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)
    img8 = cv2.rotate(img4, cv2.ROTATE_90_CLOCKWISE)
    X.append(tf.keras.utils.img_to_array(img))
    X.append(tf.keras.utils.img_to_array(img2))
    X.append(tf.keras.utils.img_to_array(img3))
    X.append(tf.keras.utils.img_to_array(img4))
    X.append(tf.keras.utils.img_to_array(img5))
    X.append(tf.keras.utils.img_to_array(img6))
    X.append(tf.keras.utils.img_to_array(img7))
    X.append(tf.keras.utils.img_to_array(img8))
    Y.extend([1, 1, 1, 1, 1, 1, 1, 1])

print("2/4 B Load", i, len(X))

# Cの画像
images1 = glob.glob(os.path.join('/content/images/C', "*.jpg"))
for i in range(len(images1)):
    img = tf.keras.utils.img_to_array((tf.keras.utils.load_img(images1[i], color_mode='rgb', target_size=targetsize)))
    img2 = cv2.flip(img, 0)
    img3 = cv2.flip(img, 1)
    img4 = cv2.flip(img, 2)
    img5 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img6 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    img7 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)
    img8 = cv2.rotate(img4, cv2.ROTATE_90_CLOCKWISE)
    X.append(tf.keras.utils.img_to_array(img))
    X.append(tf.keras.utils.img_to_array(img2))
    X.append(tf.keras.utils.img_to_array(img3))
    X.append(tf.keras.utils.img_to_array(img4))
    X.append(tf.keras.utils.img_to_array(img5))
    X.append(tf.keras.utils.img_to_array(img6))
    X.append(tf.keras.utils.img_to_array(img7))
    X.append(tf.keras.utils.img_to_array(img8))
    Y.extend([2, 2, 2, 2, 2, 2, 2, 2])

print("3/4 C Load", i, len(X))

# Doubleの画像
images4 = glob.glob(os.path.join('/content/images/D', "*.jpg"))
for i in range(len(images4)):
    img = tf.keras.utils.img_to_array((tf.keras.utils.load_img(images4[i], color_mode='rgb', target_size=targetsize)))
    img2 = cv2.flip(img, 0)
    img3 = cv2.flip(img, 1)
    img4 = cv2.flip(img, 2)
    img5 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    img6 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    img7 = cv2.rotate(img3, cv2.ROTATE_90_CLOCKWISE)
    img8 = cv2.rotate(img4, cv2.ROTATE_90_CLOCKWISE)
    X.append(tf.keras.utils.img_to_array(img))
    X.append(tf.keras.utils.img_to_array(img2))
    X.append(tf.keras.utils.img_to_array(img3))
    X.append(tf.keras.utils.img_to_array(img4))
    X.append(tf.keras.utils.img_to_array(img5))
    X.append(tf.keras.utils.img_to_array(img6))
    X.append(tf.keras.utils.img_to_array(img7))
    X.append(tf.keras.utils.img_to_array(img8))
    Y.extend([4, 4, 4, 4, 4, 4, 4, 4])
print("4/4 D Load",i, len(X))

# arrayに変換
X = np.asarray(X)
Y = np.asarray(Y)

# 学習用データとテストデータ
train_images, test_images, train_labels, test_labels = train_test_split(X, Y, test_size=0.15, random_state=111)


train_images = (train_images / 255.0 *0.99)+0.01
test_images = (test_images / 255.0 *0.99 )+0.01

print(test_images.shape)

train_images = train_images.reshape(train_images.shape[0], 128, 128, 3)
test_images = test_images.reshape(test_images.shape[0], 128, 128, 3)

# One-hot encode the labels
train_labels = tf.keras.utils.to_categorical(train_labels, 5)
test_labels = tf.keras.utils.to_categorical(test_labels, 5)
#x_test = x_test.reshape(x_test.shape[0],*image_shape)
print("Start Learning")
start = time.time()


#通常のモデル作成　Compile the model
model = tf.keras.Sequential()

model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=(128, 128, 3)))
model.add(tf.keras.layers.MaxPooling2D(pool_size=5))
model.add(tf.keras.layers.Dropout(0.5))

model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=5, padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
model.add(tf.keras.layers.Dropout(0.5))

#model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=5, padding='same', activation='relu'))
#model.add(tf.keras.layers.MaxPooling2D(pool_size=2))
#model.add(tf.keras.layers.Dropout(0.5))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dense(5, activation='softmax'))

#callback設定
#callback設定
savefilename_weights = now.strftime('%Y%m%d_%H%M') + zipfile[0][:-4] + '.weights.h5'  # ✅ 重み保存用ファイル名
savefilename_full = now.strftime('%Y%m%d_%H%M') + zipfile[0][:-4] + '_modelTF2-18.h5'       # ✅ Jetson用フルモデルファイル名

callbacklist = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy',  # ← 精度で停止条件を監視
        patience=30              # ← 30エポック変化がなければ学習停止
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath=savefilename_weights,
        monitor='val_loss',
        mode='min',
        verbose=1,
        save_best_only=True,
        save_weights_only=True  # ✅ モデル構造を含めず重みだけ保存（安全）
    ),
]

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

history = model.fit(
    train_images, train_labels,
    batch_size=32,
    epochs=200,
    callbacks=callbacklist,
    validation_data=(test_images, test_labels)
)

# 学習時間の計測結果
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# ✅ Jetson互換用の最終モデル保存（構造＋重み, オプティマイザ無し）
model.save(savefilename_full, include_optimizer=False)
print(f"✅ モデル保存完了（Jetson互換形式）→ {savefilename_full}")

# 精度評価
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# 結果データ送信（ログ）
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss)+1)

payload = {
    'starttime': now,
    'userid': zipfile[0][:-4],
    'elaptime': elapsed_time,
    'epoch': len(loss),
    'googimg': len(images1),
    'badimg': len(images0),
    'val_loss': val_loss,
    'val_acc': val_acc,
    'test_acc': test_acc
}
response = requests.get(
    "https://script.google.com/macros/s/AKfycbwV5ov8Y-PovXhbWrnhOQk01SrJ0TE875w8nUp2aJMVi9zT7LsR9enJud0qa-Gl-bxf/exec",
    params=payload
)

print("✅ Complete making Machine learning model !!")
