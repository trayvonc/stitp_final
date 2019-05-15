from aip import AipNlp
from Conn import get_Post
from Conn1 import DB

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    stopwords = stopwordslist('stopwords.dat')  # 这里加载停用词的路径
    outstr = ''
    items = client.lexer(sentence).items()
    #print("完成分词")
    if list(items)[1][1] == 'Open api qps request limit reached':
        return -1
    else:
        for i in range(len(list(items)[2][1])):
            word = list(items)[2][1][i]['item']
            if word not in stopwords:
                # print(word)
                outstr += word
                outstr += " "
        return outstr


""" 你的 APPID AK SK """
APP_ID = '14758681'
API_KEY = 'BdpeECEUdT4FPuEcMayz9txE'
SECRET_KEY = 'GGK8bFAM8ysFuaBqZOtxblPfmq62HaGS'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
f2 =open("fenci_result.txt", 'a',encoding='utf8')

#简单断句
for Post in get_Post():
    db = DB()
    #接下来，遍历所有文章，我们获取到语料库的每行数据
    #得到语句plist[0]并切割
    #print(Post[0]),字串长度受限
    if len(Post[0])>=5:
      tmp=seg_sentence(Post[0][0:49])
      while (tmp == -1):
          tmp = seg_sentence(Post[0][0:34])
      final = tmp
      f2.write(final.encode("utf8", 'ignore').decode("utf8", "ignore"))
    else:
      final = ""
    #每次都存入避免编号错位
    if db.process_item(final) == "null":
        break
    else:
        continue
f2.close()