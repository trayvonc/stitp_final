#  获取新浪新闻的标题，内容，时间，类别
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from datetime import datetime
import re
import json
import pandas
import demjson
import time
from stitp.Conn import process_item

def getNewsdetial(newsurl):
     res = requests.get(newsurl)
     res.encoding = 'utf-8'
     soup = BeautifulSoup(res.text,'html.parser')
     newsArticle = getnewsArticle(soup.select('.article p'))
     print("length : \t",len(newsArticle))
     if len(newsArticle) == 0:
         newsAuthor = ""
         newsArticle = ""
     else:
         newsAuthor = newsArticle[-1]
         newsArticle = ",".join(newsArticle[1:])
         newsArticle = newsArticle.replace('\n','').replace(',','，')
     return newsArticle
def getnewsArticle(news):
    newsArticle = []
    for p in news:
      newsArticle.append(p.text.strip())
    return newsArticle
def getNewsLinkUrl():
    urlFormat ='http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&page={}&format=json'
    url = []
    newslabel = []
    title_all = []
    newstime = []
    for i in range(76, 400):
        print("运行到第" + str(i) + '页')
        res = requests.get(urlFormat.format(i))
        res.encoding = 'gbk'
        json_string = res.text.lstrip('var jsonData = ').rstrip(';').replace("'", '"')
        json_string =json_string.replace("serverSeconds :", "\"serverSeconds\" :").replace("last_time :", "\"last_time\" :").replace("path :", "\"path\" :")
        json_string =json_string.replace("count :", "\"count\" :").replace("offset_page :", "\"offset_page\" :").replace("offset_num :", "\"offset_num\" :")
        json_string =json_string.replace("list :", "\"list\" :").replace("channel :", "\"channel\" :").replace("title: ","\"title\" :")
        json_string =json_string.replace("id :", "\"id\" :").replace("cType :", "\"cType\" :").replace("url :", "\"url\" :").replace("url :", "\"url\" :")
        json_string =json_string.replace("type :", "\"type\" :").replace("pic :", "\"pic\" :").replace("time :", "\"time\" :")
        regex = re.compile(r'\\(?![/u"])')
        json_string = regex.sub(r"\\\\", json_string)
        #print(json_string)
        print("------------------------")
        jd = demjson.decode(json_string)
        #jd = json.loads(json_string)
        #print(type(jd))
        urls, newslabels, title_alls, newstimes = getUrl(jd)
        #with open('d:/news_sina_0104.txt', 'a', encoding='utf-8') as f:

        for num in range(len(urls)):
          ar_au = getNewsdetial(urls[num])
          item = {}
          item["newslabels"]=newslabels[num]
          item["title_alls"] = title_alls[num]
          item["newstimes"] = newstimes[num]
          item["post"] = getNewsdetial(urls[num])[0:500]
          if process_item(item) == "null":
              break
          else:
              continue
          #f.writelines(newslabels[num] + '----' + title_alls[num] + '----'+newstimes[num]+'----'+ar_au+'\n')

def getUrl(jd):
    #      获取每一分页的新闻地址
    url = []
    title_all = []
    # print(jd[0])
    newslabel = []
    newstime = []
    article_all = []
    time_format = re.compile('\d{4}-\d{2}-\d{2}')
    for i in jd["list"]:
        newslabel.append(i['channel']['title'])
        title_all.append(i['title'])
        url.append(i['url'])
        time_data = re.findall(time_format, i['url'])[0]
        newstime.append(time_data)
    return url, newslabel, title_all, newstime


getNewsLinkUrl()
