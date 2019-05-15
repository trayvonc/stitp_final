#测试plot效果
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from Conn5 import *
import re


np1=np.zeros((10,2),dtype=np.int16)
#print(np1)
for a in count():
    if a[1]>np1[0][1]:
        np1[0][0]=a[0]
        np1[0][1]=a[1]

    elif a[1]>np1[1][1]:
        np1[1][0] = a[0]
        np1[1][1] = a[1]

    elif a[1]>np1[2][1]:
        np1[2][0] = a[0]
        np1[2][1] = a[1]

    elif a[1]>np1[3][1]:
        np1[3][0] = a[0]
        np1[3][1] = a[1]

    elif a[1]>np1[4][1]:
        np1[4][0] = a[0]
        np1[4][1] = a[1]

    elif a[1]>np1[5][1]:
        np1[5][0] = a[0]
        np1[5][1] = a[1]

    elif a[1]>np1[6][1]:
        np1[6][0] = a[0]
        np1[6][1] = a[1]

    elif a[1]>np1[7][1]:
        np1[7][0] = a[0]
        np1[7][1] = a[1]

    elif a[1]>np1[8][1]:
        np1[8][0] = a[0]
        np1[8][1] = a[1]

    elif a[1]>np1[9][1]:
        np1[9][0] = a[0]
        np1[9][1] = a[1]

dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
dict6={}
dict7={}
dict8={}
dict9={}
dict10={}

for d in count1(np1[0][0]):
    dict1[str(d[0])]=d[1]

for d in count1(np1[1][0]):
    dict2[str(d[0])]=d[1]

for d in count1(np1[2][0]):
    dict3[str(d[0])]=d[1]

for d in count1(np1[3][0]):
    dict4[str(d[0])]=d[1]

for d in count1(np1[4][0]):
    dict5[str(d[0])]=d[1]

for d in count1(np1[5][0]):
    dict6[str(d[0])]=d[1]

for d in count1(np1[6][0]):
    dict7[str(d[0])]=d[1]

for d in count1(np1[7][0]):
    dict8[str(d[0])] = d[1]

for d in count1(np1[8][0]):
    dict9[str(d[0])] = d[1]

for d in count1(np1[9][0]):
    dict10[str(d[0])] = d[1]



time=[]
hots=[]
dict=dict6
print(dict)
#从字典中取出键名和数值
for ti in sorted(dict.keys()):
  time.append(int(ti.replace('-','')))
for ho in dict.values():
    hots.append(ho)

#判断日期是否在数组中
alltime=[20181029,20181030,20181031,20181101,20181102,20181103,20181104,20181105,20181106,20181107,20181108,20181109,20181110,20181111]
i=0
hotss=[]
for day in alltime:
    if day in time:
        hotss.append(hots[i])
        i=i+1
    else:
        hotss.append(0)

time = np.array(time)#x轴
hots = np.array(hotss)
time=np.array(range(1,len(hots)+1))
print(time)
print(hots)
#timenew = np.linspace(time.min(), time.max(), 300)  # 300 represents number of points to make between T.min and T.max

# hots_smooth = spline(time, hots, timenew)

# plt.plot(timenew, hots_smooth)
plt.plot(time, hots)

plt.title("trend",fontsize=13)
plt.xlabel('time (day)',fontsize=12)
plt.ylabel('hot (relative)',fontsize=12)
plt.scatter(time,hots,marker='o')
plt.show()

