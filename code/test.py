# !/usr/bin/env python
# -*- coding: utf-8  -*-
# 测试训练好的模型

import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import gensim

if __name__ == '__main__':
    fdir = 'D:\\file\\pythonwork\\stitp\\'
    model = gensim.models.Word2Vec.load(fdir + 'wiki.zh.text.model')
    #输出网络的词向量
    #print(model["网络"])
    #print(model.wv.vocab.keys())
    #输出和网络最相近的词
    word = model.most_similar(u"欧盟")

    for t in word:
        print(t[0], t[1])




