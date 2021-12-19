import cv2
import numpy as np
import matplotlib.pyplot as plt

imgList = [
    cv2.imread(r'D:/Program/reefStudy/data/gr2018.png'),
    cv2.imread(r'D:/Program/reefStudy/data/gr2019.png'),
    cv2.imread(r'D:/Program/reefStudy/data/gr2020.png')
]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def access_pixels(img):
    cnt = 0
    height = img.shape[0]        #将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]
    for row in range(height):    #遍历每一行
        for col in range(width): #遍历每一列
            for channel in range(channels):    #遍历每个通道（二值化后只有一个通道）
                val = img[row][col][channel]
                if (val) >= 100:
                    cnt+=1
    return cnt

ans = []
for i in imgList:
    num = access_pixels(i)
    ans.append(num)
plt.plot(ans)
plt.title("2018-2020全球珊瑚礁存活数量(相对)")
plt.show()

    