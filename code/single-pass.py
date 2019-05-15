# encoding=utf-8
from numpy import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
from stitp.Conn import *
#reload(sys)
#sys.setdefaultencoding('utf8')

#stopwords = [line.strip().decode('utf-8') for line in open('stopwords.dat',encoding='utf-8').readlines()]
theta=0.40
xClusterID=2

def getTfidfMat(lst):#测试函数
    # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
    vectorizer = CountVectorizer()
    # 该类会统计每个词语的tf-idf权值
    transformer = TfidfTransformer()
    # 第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
    tfidf = transformer.fit_transform(vectorizer.fit_transform(lst))
    # 获取词袋模型中的所有词语
    word = vectorizer.get_feature_names()
    # 将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
    weight = tfidf.toarray()
    #词频cp=vectorizer.fit_transform(lst)
    #词频cp=cp.toarray()
    # for i in range(len(weight)):
    #     for j in range(len(word)):
    #         print word[j],cp[i][j],'#',
    #     print '\n'
    return weight


if __name__ == "__main__":
    #开始single-pass部分

        #resList1 = db.cur.execute("Select Id,fenci from roll WHERE isProcessed=0 AND newslabels='体育'")
        #resList1=db.get_unfenlei(db)
        #for ID0, fenci0 in resList1:
    for unfenlei in get_unfenlei():
        ####更新weightMat
        ID0=unfenlei[0]
        fenci0=unfenlei[1]
        if fenci0 ==None:
            continue
        #corpus = []
        trClusterID = []
        fencilist1=[]
        #print(ID0)
        #print(fenci0)

            #resList = db.cur.execute("SELECT Id,fenci,ClusterID,isProcessed FROM roll WHERE isProcessed=1,newslabels='体育'")
            #for (ID1, fenci1,ClusterID, isProcessed) in resList:
        for isfenlei in get_isfenlei():
           # corpus.append(content1)
            ID1=isfenlei[0]
            fenci1=isfenlei[1]
            if fenci1 ==None:
                continue
            ClusterID=isfenlei[2]
            trClusterID.append(ClusterID)
            fencilist1.append(fenci1)

        #segedTxtlst = fenci(corpus)

        vectorizer = TfidfVectorizer()
        trainTfidf = vectorizer.fit_transform(fencilist1)
        weightMat = trainTfidf.toarray()  # 得到语料库的VSM
        ####更新weightMat结束

        fencilist0=[]
        fencilist0.append(fenci0)
        testTfidf = vectorizer.transform(fencilist0)
        testVec = testTfidf.toarray()#得到基于tf-idf的文档向量
        # 计算testVec和weightMat每一行的余弦相似度
        xx = cosine_similarity(testVec, weightMat)
        ndxx=array(xx)
        max=ndxx.max()
        if(max>theta):
            indxx=argmax(ndxx)#最大值在weightMat的index已经找到
            update(trClusterID[indxx],ID0)
        else:
            # 不大于某阈值就新建一个分类
            update(xClusterID,ID0)
            xClusterID+=1
            #已经把一条新闻聚到某个簇了，下面要更新一下weightMat
