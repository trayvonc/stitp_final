# -*- coding: utf-8 -*-
from collections import defaultdict
import math
import operator
from Conn3 import get_Data
from Conn4 import DB
from Conn5 import count,hottitle
import numpy as np
import os
"""
函数说明:创建数据样本
Returns:
    dataset - 实验样本切分的词条
    classVec - 类别标签向量
"""
def loadDataSet():
    dataset=[]
    classVec=[]
    for Data in get_Data():
        if(Data[3]==1):
            dataset.append(Data[1].split(" "))# 切分的词条
            classVec.append(Data[2])
    return dataset, classVec
 
 
"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
"""
def feature_select(list_words):
    #总词频统计
    doc_frequency=defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i]+=1
 
    #计算每个词的TF值
    word_tf={}  #存储没个词的tf值
    for i in doc_frequency:
        word_tf[i]=doc_frequency[i]/sum(doc_frequency.values())
 
    #计算每个词的IDF值
    doc_num=len(list_words)
    word_idf={} #存储每个词的idf值
    word_doc=defaultdict(int) #存储包含该词的文档数
    for i in doc_frequency:
        for j in list_words:
            if i in j:
                word_doc[i]+=1
    for i in doc_frequency:
        word_idf[i]=math.log(doc_num/(word_doc[i]+1))
 
    #计算每个词的TF*IDF的值
    word_tf_idf={}
    for i in doc_frequency:
        word_tf_idf[i]=word_tf[i]*word_idf[i]
 
    # 对字典按值由大到小排序
    dict_feature_select=sorted(word_tf_idf.items(),key=operator.itemgetter(1),reverse=True)
    return dict_feature_select

def fenlei():
    np1 = np.zeros((10, 2),dtype=np.int16)
    for a in count():
        if a[1] > np1[0][1]:
            np1[0][0] = a[0]
            np1[0][1] = a[1]

        elif a[1] > np1[1][1]:
            np1[1][0] = a[0]
            np1[1][1] = a[1]

        elif a[1] > np1[2][1]:
            np1[2][0] = a[0]
            np1[2][1] = a[1]

        elif a[1] > np1[3][1]:
            np1[3][0] = a[0]
            np1[3][1] = a[1]

        elif a[1] > np1[4][1]:
            np1[4][0] = a[0]
            np1[4][1] = a[1]

        elif a[1] > np1[5][1]:
            np1[5][0] = a[0]
            np1[5][1] = a[1]

        elif a[1] > np1[6][1]:
            np1[6][0] = a[0]
            np1[6][1] = a[1]

        elif a[1] > np1[7][1]:
            np1[7][0] = a[0]
            np1[7][1] = a[1]

        elif a[1] > np1[8][1]:
            np1[8][0] = a[0]
            np1[8][1] = a[1]

        elif a[1] > np1[9][1]:
            np1[9][0] = a[0]
            np1[9][1] = a[1]
    return np1


if __name__=='__main__':
    #f = open("tf_idf.txt", 'a', encoding='utf8')
    #db = DB()
    print('runing tf_idf...')
    data_list,label_list=loadDataSet() #加载数据
    features=feature_select(data_list) #所有词的TF-IDF值
    #print(features)
    #print(len(features))
    print('runing division...')
    np=fenlei()
    list = [([] * 1) for i in range(10)]
    list1 = []
    res = [([] * 1) for i in range(10)]
    for i in range(0, 10):
        for abc in hottitle(np[i][0]):
          list[i].append(abc[0])
    #print(list[0][0]+list[0][1])
    for i in range(len(list)-1):
      temp=''
      for j in range(len(list[i])-1):
          temp = temp+list[i][j]
      list1.append(temp)

    #与features对比
    # list3=[]
    # for i in range(len(list1)):
    #     aa = list1[i].split(' ')
    #     for t in range(len(features) - 1):
    #         for s in range(len(aa) - 1):
    #             if (aa[s] == features[t][0]):
    #                 print(aa[s],end=' ')
    #     print('---------------------------')
    # print(list3[0])




    for i in range(len(list1)-1):
        temp = list1[i].split(' ')
        list1[i] = []
        for j in range(len(temp)-1):
            list1[i].append(temp[j])


    #print(list1)



    features_str = []
    #print(features)
    for i in range(len(features)-1):
        features_str.append(features[i][0])

    result = []
    for i in range(len(list1)-1):
        line = []
        for j in range(len(features_str)-1):
            if(features_str[j] in list1[i] and features_str[j] not in line):
                line.append(features_str[j])
        result.append(line)

    print(result)










