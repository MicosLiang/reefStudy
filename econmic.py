import csv
import numpy as np
import matplotlib.pyplot as plt
import math

from matplotlib.font_manager import FontProperties
fonts = FontProperties(fname=r'C:windowsfontssimsun.ttc',size=64)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

radius = 100

def max(arr):
    m = 0
    for i in arr:
        if i > m:
            m = i
    return m

def __main__():
    global radius
    data = []
    with open(r'./data/econmic.csv', 'r', encoding='utf-8') as f:
        fcsv = csv.reader(f)
        for row in fcsv:
            data.append(row)

    top = []
    for i in data:
        arr =  []
        cnt = 0
        for k in i:
            k = int(k)
            i[cnt] = k
            try:
                arr[cnt].append(k)
            except:
                arr.append([])
                arr[cnt].append(k)
            cnt+=1
    for i in arr:
        top.append(max(i))

    plt.figure(figsize=(6,4))    

    for i in data:
        leng = len(i)
        x = []
        y = []
        cnt = 0
        for k in i:
            tx = radius * math.cos((cnt/leng)*6.28) + radius
            # tx = cnt
            try:
                ty = radius * (k/top[cnt]) * math.sin((cnt/leng)*6.28)
                # ty = k
            except:
                ty = 0
            x.append(tx)
            y.append(ty)
            plt.plot(x, y)
            cnt+=1
    plt.legend(['海洋','远洋','海岸','海湾','海草','珊瑚礁','大陆架'])
    plt.show()
    pass

__main__()