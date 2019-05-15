from stitp.Conn import *
import numpy as np
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

#print(np1)
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
    dict1[str(d[0])] = d[1]

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

print(dict1)
print(dict2)
print(dict3)
print(dict4)
print(dict5)
print(dict6)
print(dict7)
print(dict8)
print(dict9)
print(dict10)
for i in range(0,10):
   print("热度排名", i + 1)
   for abc in hottitle(np1[i][0]):
       print(abc[0])

   print("-----------------------------------------------")
