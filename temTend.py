from typing import Sized
import matplotlib.pyplot as plt
import cv2
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

tem2018 = cv2.imread(r"D:/Program/reefStudy/data/tem2018.png",0)
tem2019 = cv2.imread(r"D:/Program/reefStudy/data/tem2019.png",0)
tem2020 = cv2.imread(r"D:/Program/reefStudy/data/tem2020.png",0)
tem2021 = cv2.imread(r"D:/Program/reefStudy/data/tem2021.png",0)

bleach = cv2.imread(r'D:/Program/reefStudy/data/bleachalertspot2018.jpg',0)

def calHist(img):
    # img = cv2.resize(img, (657, 398))
    img = cv2.calcHist([img], [0], None, [256], [25.0, 255.0])
    img = cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX, -1)
    return img

def delImg(img):
    img = cv2.resize(img, (657, 398))
    return img

# plt.subplot(2,1,1)
tem2020 = delImg(tem2020)
tem2019 = delImg(tem2019)
bleach = delImg(bleach)
tmp = cv2.subtract(tem2020,tem2019)
plt.subplot(2,1,1)
plt.plot(calHist(tmp))
plt.title("原始")
tmp = cv2.subtract(tmp,bleach)
plt.subplot(2,1,2)
plt.plot(calHist(tmp))
plt.title("叠加")
plt.show()
