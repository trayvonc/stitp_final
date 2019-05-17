from aip import AipNlp
from stitp.Conn import *

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    stopwords = stopwordslist('stopwords.dat')  # 这里加载停用词的路径
    outstr = ''
    items = client.lexer(sentence).items()
    for i in range(len(list(items)[2][1])):
        word=list(items)[2][1][i]['item']
        if word not in stopwords:
                #print(word)
                outstr += word
                outstr += " "
    return outstr


""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
f2 =open("fenci_result.txt", 'a',encoding='utf8')

#简单断句

for Post in get_Post():
    #接下来，遍历所有文章，我们获取到语料库的每行数据
    #得到语句plist[0]并切割
    #print(Post[0]),字串长度受限
    if len(Post[0])>=5 and len(Post[0])<=149:
      final=seg_sentence(Post[0][:])
      f2.write(final.encode("utf8", 'ignore').decode("utf8", "ignore"))
      process_item2(final,Post[1])

    #if len(Post[0])>150:
      #final=seg_sentence(Post[0][0:149])
      #f2.write(final.encode("utf8", 'ignore').decode("utf8", "ignore"))
      #process_item2(final,Post[1])

f2.close()
