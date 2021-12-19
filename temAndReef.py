from typing import Sized
import matplotlib.pyplot as plt
import cv2
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree

def classify_hist_with_split(image1, image2, size=(255,255)):
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data


tem2018 = cv2.imread(r"D:/Program/reefStudy/data/tem2018.png")
tem2019 = cv2.imread(r"D:/Program/reefStudy/data/tem2019.png")
tem2020 = cv2.imread(r"D:/Program/reefStudy/data/tem2020.png")
tem2021 = cv2.imread(r"D:/Program/reefStudy/data/tem2021.png")

picList = [tem2018,tem2019,tem2020,tem2021]

tem2018 = cv2.resize(tem2018, (657,398))
tem2019 = cv2.resize(tem2019, (657,398))
tem2020 = cv2.resize(tem2020, (657,398))
tem2021 = cv2.resize(tem2021, (657,398))

# tmp1 = cv2.addWeighted(tem2018,0.5,tem2019,0.5,0)
# tmp2 = cv2.addWeighted(tem2020,0.5,tem2021,0.5,0)
# tmp3 = cv2.addWeighted(tmp1,0.5,tmp2,0.5,0)

# globalreef = cv2.imread(r"D:/Program/reefStudy/data/gr2020.png")
# globalreef = cv2.resize(globalreef, (657,398))

# tmp3 = cv2.subtract(tem2021,tem2020)
# print(classify_hist_with_split(tmp3,tem2021))
# tmp3 = cv2.addWeighted(globalreef,0.8,tmp3,0.2,0)

gr2018 = cv2.imread(r"D:/Program/reefStudy/data/gr2018.png")
gr2019 = cv2.imread(r"D:/Program/reefStudy/data/gr2019.png")
gr2020 = cv2.imread(r"D:/Program/reefStudy/data/gr2020.png")

plt.plot([0.24361189,0.2487901])
plt.plot([0.22682571411132812,0.266563355922699])
plt.legend(["水温变化速率","珊瑚变化速率"])
plt.title("水温变化速率和珊瑚变化速率比较")
plt.show()



# tmp3 = cv2.cvtColor(tmp3, cv2.COLOR_BGR2GRAY)


# cv2.imshow('tmp3',tmp3)
# cv2.waitKey()