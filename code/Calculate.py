#计算每一个文档的向量
from stitp.Conn2 import get_Post
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import gensim
import numpy as np


def get_list():
 i = 0
 fdir = 'D:/file/pythonwork/stitp/'
 model = gensim.models.Word2Vec.load(fdir + 'wiki.zh.text.model')
 for Post in get_Post():
    #接下来，遍历所有文章，我们获取到分割后的每行数据
    #得到语句post[0]
    #print(type(Post[0]))
    #i+=1
    if Post[0]!=None and len(Post[0])>5:
        #取出一行，按空格间隔存入list
        lists=Post[0].split(" ")
        #print(list)
        #return list
        #因为最后包含一个空格，长度要减一
        length=len(lists)-1
        sum=[0]*400

        for l in range(len(lists)-1):
           word=lists[l]
         #加载该词的向量,有些词不在句子中要排除
           if word in model.wv.vocab:
             sum+=model[word]
           else:
               length=length-1
       # print(i)
        res=sum/length
        # return res
    else:
        res=[0]*400
    #print(list(res))
    # 存入数据
    a=list(res)
    #print(type(res.tolist()))
    f.write(" ".join('%s' %id for id in a))
    f.write("\n")
 f.close()


f = open("calculate_result.txt", 'a', encoding='utf8')
get_list()