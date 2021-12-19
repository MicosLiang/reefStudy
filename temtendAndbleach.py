from typing import Sized
import matplotlib.pyplot as plt
import cv2
import numpy as np

tend = cv2.imread(r'D:/Program/reefStudy/data/temtend2018.jpg')
# bleach = cv2.imread(r'D:/Program/reefStudy/data/bleachspot2018.jpg')
bleach = cv2.imread(r'D:/Program/reefStudy/data/bleachalertspot2018.jpg')

tend = cv2.resize(tend,(600,400))
bleach = cv2.resize(bleach, (600,400))

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# tmp = cv2.addWeighted(tend,0.5,bleach,0.5,0)
# cv2.imshow('tmp', tmp)

# bleach = cv2.cvtColor(bleach, cv2.COLOR_BGR2GRAY)
# tend = cv2.cvtColor(tend, cv2.COLOR_BGR2GRAY)
# calculate(bleach,tend)

# cv2.waitKey()

def huidu(img):
    img = cv2.resize(img,(657,398))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.calcHist([img], [0], None, [256], [25.0, 255.0])
    img = cv2.normalize(img,img,0,1,cv2.NORM_MINMAX,-1)
    return img

gr2018 = cv2.imread(r"D:/Program/reefStudy/data/gr2018.png", 0)
gr2019 = cv2.imread(r"D:/Program/reefStudy/data/gr2019.png", 0)
gr2020 = cv2.imread(r"D:/Program/reefStudy/data/gr2020.png", 0)

t1 = huidu(gr2018)
t2 = huidu(gr2019)
t3 = huidu(gr2020)

# plt.subplot(2,1,1)
# plt.plot(t1)
# plt.title("2018")
plt.subplot(2,1,2)
plt.plot(t2)
plt.title("2019")
plt.subplot(2,1,2)
plt.plot(t3)
plt.title("2020")
plt.show()