#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import pymysql


def process_item(item):
    """ 判断item的类型，并作相应的处理，再入数据库 """
    if isinstance(item,dict):
        # if self.data.find_one({"nickname":item["nickname"],"Post":item["Post"],"Pubtime":item["Pubtime"]}):
        #      return "null"
        # else:
            # self.data.insert(item)
        cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
        cur = cnxn.cursor()
        cur.execute(
            "insert into roll2(newslabels, title_alls, newstimes, post) values(%s, %s, %s, %s)",
            (item["newslabels"], item["title_alls"],item["newstimes"],item["post"]
             ,))
        cnxn.commit()
        cnxn.close()
        print("insert data into database...")
        return "ok"

def process_item2(final,id):
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    cur.execute(
     "update roll set fenci=%s where Id=%s",
      (final,id,))
    cnxn.commit()
    cnxn.close()
    #print("insert data into database...")
    return "ok"

def get_Post():
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    select = "Select post,Id from roll"
    cur.execute(select)
    row = cur.fetchall()
    # row = cur.fetchone()
    if row:
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
    cnxn.close()

#读出未分类的新闻
def get_unfenlei():
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    select ="Select Id,res from roll WHERE isProcessed040=0 AND newslabels='财经'"
    cur.execute(select)
    row = cur.fetchall()
    if row:
        cnxn.close()
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
        cnxn.close()
        return 0

def get_isfenlei():
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    select = "Select Id,res,ClusterID040 from roll WHERE isProcessed040=1 AND newslabels='财经'"
    cur.execute(select)
    row = cur.fetchall()
    if row:
        cnxn.close()
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
        cnxn.close()
        return 0

def update(cd,id):
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    cur.execute("UPDATE  roll set ClusterID040='%d',isProcessed040=1 WHERE Id=%s" % (cd,id))
    cnxn.commit()
    cnxn.close()

def count():
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    #cur.execute("SELECT COUNT(*) FROM roll GROUP BY ClusterID040")
    cur.execute("select ClusterID040,count(*) as count from roll WHERE isProcessed040=1 AND newslabels='科技' group by ClusterID040 having count>1")
    row = cur.fetchall()
    if row:
        cnxn.close()
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
        cnxn.close()
        return 0

def count1(cd):
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    #cur.execute("SELECT COUNT(*) FROM roll GROUP BY ClusterID040")
    select ="select newstimes,count(*) as count from roll WHERE ClusterID040='%d' AND newslabels='科技' group by newstimes having count>0" % (cd)
    cur.execute(select)
    row = cur.fetchall()
    if row:
        cnxn.close()
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
        cnxn.close()
        return 0

def hottitle(cd):
    cnxn = pymysql.connect(host="localhost", user="root", password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    select = "Select title_alls from roll WHERE ClusterID040='%d' AND newslabels='科技'"% (cd)
    cur.execute(select)
    row = cur.fetchall()
    if row:
        cnxn.close()
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
        cnxn.close()
        return 0










